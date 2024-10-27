const Category = require("./Category")
const slugify = require('slugify')


function categoriaRoot(req, res){

    Category.findAll({
        raw: true,
        order: [['id', 'DESC']]
    }).then(categories => {
        res.render('admin/categories/index', 
            {categories: categories})
    })

}

function categoriaEditar(req, res){
    
    var id_cat = req.params.id_cat

    if(isNaN(id_cat)){
        res.redirect("/categorias/")
    }

    if (id_cat != undefined){

        Category.findByPk(id_cat).then(categoria => {
            if (categoria != undefined){

                res.render('admin/categories/edit', {categoria: categoria})

            }else{
                res.redirect("/categorias/")
            }
        }).catch(erro => {
            res.redirect("/categorias/")
        })

    } else {
        
        res.redirect("/categorias/")
    }

}

function categoriaCadastro(req, res){

    res.render('admin/categories/cadastro')

}

function categoriesSave(req, res){

    var title = req.body.title
    var id_cat = req.body.id_cat

    if(id_cat != undefined){

        Category.update({
            title: title,
            slug: slugify(title)
        }, {where: {id: id_cat}}).then(() => {
            res.redirect("/categorias/")
        })
        
    } else if(title != undefined){

        Category.create({
            title: title,
            slug: slugify(title)
        }).then(() => {
            res.redirect("/categorias/")
        })

    } else {
        res.redirect("/categorias/")
    }
}

function categoriesDelete(req, res){
    
    var id = req.body.id;

    if(id != undefined){

        if(!isNaN(id)){

            Category.destroy({
                where: {
                    id: id
                }
            }).then(() => {
                res.redirect("/categorias/")
            })

        }
        else
        {
            res.redirect("/categorias/")
        }
    }
    
    else
    {
        res.redirect("/categorias/")
    }
}

module.exports = {
    
    categoriaRoot,
    categoriaCadastro,
    categoriaEditar,
    categoriesSave,
    categoriesDelete

}