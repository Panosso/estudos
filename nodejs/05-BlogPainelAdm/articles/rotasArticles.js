const Article = require("./Article")
const Category = require("../categories/Category")
const slugify = require('slugify')

function artigoRoot(req, res){
    Article.findAll({
        include: [{model: Category}]
    }).then(articles => {
        res.render("admin/articles/index", {articles: articles})        
    })

}

function artigoCadastro(req, res){
    
    Category.findAll().then(categories => 
        res.render('admin/articles/cadastro', {categories: categories})
    )

}


// artigoEditar

function artigoSave(req, res){

    var title = req.body.title;
    var textbody = req.body.textbody;
    var category = req.body.category
 
    Article.create({title: title,
                    slug: slugify(title),
                    body: textbody,
                    categoryId: category
    }).then(() => {
        res.redirect("/artigos/")
    })
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
    artigoDelete
}