const express = require('express')
const bodyParser = require('body-parser')
const session = require('express-session')
const app = express()
const port = 4000

const conn = require('./database/database.js')
const categoriesController = require('./categories/CategoriesController.js')
const articleController = require('./articles/ArticlesController.js')
const userController = require('./user/UserController.js')
const rotas = require('./rotas.js')

const Category = require("./categories/Category.js")
const Article = require("./articles/Article.js")
const User = require("./user/User.js")

conn.connection
    .authenticate()
    .then(() => {
        console.log("conn executada com sucesso")
    })
    .catch((msgErro) => {
        console.log(msgErro)
    })

app.set('view engine', 'ejs')

app.use(session({
    //secret é um valor aleatorio que será usado durante a app
    //cookie, são configs do cookie, o maxAge recebe um valor em milisegundos para saber quanto tempo ela ira durar
    secret: "qualquercoisa", cookie: {maxAge: 30000}
}))

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())


app.get("/", rotas.root)
app.get("/session", rotas.userSession)
app.get("/leitura", rotas.userReader)
app.get("/articles/:articleSlug", rotas.articleSlug)
app.get("/categorie/:categorieSlug", rotas.categorieSlug)

//Com esse controler é utilizado para definir as rotas, nele é necessário um prefixo:
//esse prefixo define o que precisa ser digitado antes de acessar o link
app.use("/categorias", categoriesController)
app.use("/artigos", articleController)
app.use("/usuarios", userController)


app.listen(port, function(erro){

    if (erro){
        console.log("Ocorreu um erro")
    } else {
        console.log("Servidor iniciado com sucesso")
    }

})
