const Sequelize = require('sequelize');

const connection = new Sequelize('guiapress', 'root', 'Sql!@#Qwe456', {
    host: '127.0.0.1',
    dialect: 'mysql',
    timezone: "-03:00"
})

module.exports = {
    connection
}
