const Category = require("./categories/Category")
const Article = require("./articles/Article")
const slugify = require('slugify')

function root(req, res){

    Article.findAll({
        order:[
            ['id', 'DESC']
        ],
        limit:4
    }).then(articles => {
        Category.findAll().then(categories => {
            res.render("html/raiz", {articles: articles, categories: categories})
        })
    })


}

function articleSlug(req, res){

    var slug = req.params.articleSlug
    
    console.log(slug)

    Article.findOne({
        where: {
            slug: slug
        }
    }).then(article => {
        if(article != undefined){
            Category.findAll().then(categories => {
            res.render("html/articles", {article: article, categories: categories})
            })
        }else{
            res.redirect("/")
        }
    }).catch(erro => {
        res.redirect("/")
    })
}

function categorieSlug(req, res){

    var slug = req.params.categorieSlug

    console.log(slug);
    

    Category.findOne({
        where: {
            slug: slug
        },
        include: [{model: Article}
        ]
    }).then( category => {
        Category.findAll().then( categories => {
            res.render("html/raiz", {articles: category.articles, categories: categories})
        }
        )
    }).catch(erro => {
        res.redirect("/")
    })

}


function userSession(req, res){

    req.session.treinamento = 'Teste queda livre'
    req.session.ano = 2019
    req.session.email = 'pero@pero.com'
    req.session.user = {
        username: 'pedro',
        senha: '123',
        id: 10
    }
    res.send('Deu certo')

}

function userReader(req, res){
    res.json({
        treinamento: req.session.treinamento,
        ano: req.session.ano,
        email: req.session.email,
        user: req.session.user
    })
}

module.exports = {
    root,
    articleSlug,
    categorieSlug,
    userSession,
    userReader
}