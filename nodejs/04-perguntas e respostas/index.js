const express = require('express')
const rotas = require('./rotas.js')
const conn = require('./database/database.js')
const bodyParser = require('body-parser')
const app = express()
const port = 4000

conn.connection
    .authenticate()
    .then(() => {
        console.log("conn executada com sucesso")
    })
    .catch((msgErro) => {
        console.log(msgErro)
    })

//Indicando para o express utilizar o ejs
app.set('view engine', 'ejs')

//Indicando que serão utilizados arquivos estáticos, informando o nome da pasta que contem os arquivos estaticos
app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

app.get('/', rotas.raiz)
app.get('/home', rotas.home)
app.get('/perguntar', rotas.perguntar)
app.get('/pergunta/:id', rotas.pergunta)

app.post('/salvarpergunta', rotas.salvarpergunta)



app.listen(port, function(erro){

    if (erro){
        console.log("Ocorreu um erro")
    } else {
        console.log("Servidor iniciado com sucesso")
    }

})

