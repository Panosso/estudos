const express = require('express') //Importando o express
const rotas = require('./rotas.js')
const app = express() // Iniciando e aplicando o express para a variavel constante app
const port = 4000

// As rotas devem ser criadas antes de abrir o servidor
app.get('/', rotas.raiz)

//parametro opcional, se não passar não tem problema
app.get('/blog/:artigo?', rotas.blog)
app.get('/canal', rotas.canal)
app.get('/youtube', rotas.youtube)

//parametro obrigatorio, se não passar da erro.
app.get('/ola/:nome/:empresa', rotas.ola)
app.get('/ola', rotas.ola)

app.listen(port, function(erro){

    if (erro){
        console.log("Ocorreu um erro")
    } else {
        console.log("Servidor iniciado com sucesso")
    }

})

