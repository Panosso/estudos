const express = require('express')
const jwt = require('jsonwebtoken')
require('dotenv').config()

const servidor = express()

function verificaToken(req, res, next) {
    const token = req.headers['x-access-token']

    if(!token){
        res.status(401).json({autenticacao: false, mensagem: "Token Invalido"})
    }

    const SECRET = process.env.SECRET

    jwt.verify(token, SECRET, function(error, decoded) {
        if(error){
            res.status(500).json({autenticacao: false, mensagem: "Falha ao validar token"})
        }

        req.usuarioId = decoded.id;
        next()
    })
}

servidor.use(verificaToken)

const filmes = [
    {id: 1, nome: "X-man", status: "Não vi"}
]

servidor.use(express.json())

servidor.get("/ola", (req, res) => {
    res.send('Olá Mundo!!!')
})

servidor.get("/filmes", (req, res) => {
    
    res.send(filmes)
})

servidor.post("/filmes", (req, res) => {
    filmes.push(req.body)
    res.send(filmes)
})

servidor.post("/login", (req, res, next) => {
    const { usuario, senha } = req.body;

    if(usuario === 'pedro' && senha === "123456"){
        const SECRET = process.env.SECRET

        const id = 1
        const token = jwt.sign({id}, SECRET,
            {
                expiresIn: 300
            }
        )

        return res.json({autenticacao: true, token: token})

    }

    return res.status(500).send("Usuário ou senha incorreto")

})

servidor.listen(3000, () => {
    console.log("Servidor rodando porta 3000")
})
