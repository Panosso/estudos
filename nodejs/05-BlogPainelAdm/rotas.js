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

module.exports = {
    root,
    articleSlug,
    categorieSlug
}