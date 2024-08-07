const Category = require("./categories/Category")
const slugify = require('slugify')

function root(req, res){

    res.render("html/raiz")

}

module.exports = {
    root
}