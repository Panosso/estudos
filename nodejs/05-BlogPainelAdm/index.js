const express = require('express')
const bodyParser = require('body-parser')
const app = express()
const port = 4000

const conn = require('./database/database.js')
const categoriesController = require('./categories/CategoriesController.js')
const articleController = require('./articles/ArticlesController.js')
const rotas = require('./rotas.js')

const Category = require("./categories/Category.js")
const Article = require("./articles/Article.js")

conn.connection
    .authenticate()
    .then(() => {
        console.log("conn executada com sucesso")
    })
    .catch((msgErro) => {
        console.log(msgErro)
    })

app.set('view engine', 'ejs')

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

//Com esse controler é utilizado para definir as rotas, nele é necessário um prefixo:
//esse prefixo define o que precisa ser digitado antes de acessar o link
app.use("/categorias", categoriesController)
app.use("/artigos", articleController)

app.use("/", rotas.root)


app.listen(port, function(erro){

    if (erro){
        console.log("Ocorreu um erro")
    } else {
        console.log("Servidor iniciado com sucesso")
    }

})
