const Article = require("./Article")
const slugify = require('slugify')

function artigoRoot(req, res){
    res.render("admin/articles/index")
}

function artigoCadastro(req, res){
    
    res.render('admin/articles/cadastro')
}

// artigoCadastro

// artigoEditar

// artigoSave

// artigoDelete

module.exports = {
    artigoRoot,
    artigoCadastro
}