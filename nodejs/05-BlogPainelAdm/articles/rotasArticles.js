const Article = require("./Article")
const Category = require("../categories/Category")
const slugify = require('slugify')

function artigoRoot(req, res){
    Article.findAll({
        include: [{model: Category}],
        order: [
            ['id', 'DESC']
        ],
        limit: 4
    }).then(articles => {
        res.render("admin/articles/index", {articles: articles})        
    })

}

function artigoCadastro(req, res){
    
    Category.findAll().then(categories => 
        res.render('admin/articles/cadastro', {categories: categories})
    )

}


function artigoEditar(req, res){
    var id_art = req.params.id_art

    if(isNaN(id_art)){
        res.redirect("/categorias/")
    }

    if (id_art != undefined){
        Article.findByPk(id_art).then(article => {
            Category.findAll().then(categories => {
                res.render("admin/articles/edit", {article: article, categories: categories})
            })
            
        }).catch(erro => {
            res.redirect("/artigos/")            
        })

    }else{
        res.redirect("/artigos/")
    }

}


function artigoPag(req, res){
    var page = req.params.num
    var offset = 0

    if(isNaN(page) || page == 1 ){

        offset = 0;

    } else {

        offset = (parseInt(page) -1 ) * 4

    }


    Article.findAndCountAll({
        limit: 4,
        offset: offset,
        order: [
            ['id', 'DESC']
        ]
    }).then(articles => {

        var next
        if(offset + 4 >= articles.count){
            next = false
        } else {
            next = true
        }

        var result = {
            page: parseInt(page),
            next: next,
            articles: articles
        }

        Category.findAll().then(categories => {
            res.render("admin/articles/page", {
                result: result, 
                categories: categories
            })
        })

    })

}

function artigoSave(req, res){

    var title = req.body.title;
    var textbody = req.body.textbody;
    var category = req.body.category
    var id_art = req.body.id_art
    

    if(id_art != undefined){

        console.log(id_art);
        Article.update({
            title: title,
            slug: slugify(title),
            body: textbody,
            categoryId: category
        }, {where: {id: id_art}}).then(() => {
            res.redirect("/artigos/")
        })

    }else{
        Article.create({
            title: title,
            slug: slugify(title),
            body: textbody,
            categoryId: category
        }).then(() => {
        res.redirect("/artigos/")
        })
    }

}

function artigoDelete(req, res){
    
    var id = req.body.id;

    if(id != undefined){

        if(!isNaN(id)){

            Article.destroy({
                where: {
                    id: id
                }
            }).then(() => {
                res.redirect("/artigos/")
            })

        }
        else
        {
            res.redirect("/artigos/")
        }
    }

    else
    {
        res.redirect("/artigos/")
    }
}

module.exports = {
    artigoRoot,
    artigoCadastro,
    artigoSave,
    artigoDelete,
    artigoEditar,
    artigoPag
}