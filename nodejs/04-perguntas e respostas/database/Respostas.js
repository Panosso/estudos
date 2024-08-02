const Sequelize = require("sequelize")
const conn = require("./database.js")
const { type } = require("express/lib/response")

const Resposta = conn.connection.define('respostas', {
    corpo: {
        type: Sequelize.TEXT,
        allowNull: false
    },
    perguntaId: {
        type: Sequelize.INTEGER,
        allowNull: false
    }

})

Resposta.sync({force: false})

module.exports = Resposta