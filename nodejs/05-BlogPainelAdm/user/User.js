const Sequelize = require('sequelize')
const conn = require("../database/database.js")

const User = conn.connection.define('users', {
    email: {
        type: Sequelize.STRING,
        allowNull: false
    },
    password: {
        type: Sequelize.STRING,
        allowNull: false
    }
})

User.sync({force: false});

module.exports = User;