const express = require('express')
const rotas = require('./rotas.js')
const app = express()
const port = 4000

//Indicando para o express utilizar o ejs
app.set('view engine', 'ejs')

//Indicando que serão utilizados arquivos estáticos, informando o nome da pasta que contem os arquivos estaticos
app.use(express.static('public'));

app.get('/:nome/:lenght', rotas.raiz)
app.get('/home', rotas.home)
app.get('/perguntar', rotas.perguntar)

app.listen(port, function(erro){

    if (erro){
        console.log("Ocorreu um erro")
    } else {
        console.log("Servidor iniciado com sucesso")
    }

})

