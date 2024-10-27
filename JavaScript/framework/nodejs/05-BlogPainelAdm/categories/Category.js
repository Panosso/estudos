const Sequelize = require('sequelize')
const conn = require("../database/database.js")

const Category = conn.connection.define('categories', {
    title: {
        type: Sequelize.STRING,
        allowNull: false
    },
    slug: {
        type: Sequelize.STRING,
        allowNull: false
    }
})


// Category.sync({force: true});

module.exports = Category;