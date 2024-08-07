const Sequelize = require('sequelize')
const conn = require("../database/database.js")
const Category = require('../categories/Category.js')

const Article = conn.connection.define('articles', {
    title: {
        type: Sequelize.STRING,
        allowNull: false
    },
    slug: {
        type: Sequelize.STRING,
        allowNull: false
    },
    body: {
        type: Sequelize.TEXT,
        allowNull: false
    }
})

//Uma categoria tem varias artigos --> relacionamento 1-> N
Category.hasMany(Article);

//Um artigo pertence a uma categoria --> relacionamento 1 -> 1
Article.belongsTo(Category);

//Sempre que a aplicação for iniciada será criada as tabelas
// Article.sync({force: true})

module.exports = Article;