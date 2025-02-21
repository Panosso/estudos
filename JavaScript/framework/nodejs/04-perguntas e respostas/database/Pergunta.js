const Sequelize = require('sequelize');
const conn = require('./database.js')

//Criando o model para o banco
const Pergunta = conn.connection.define('perguntas', {
    //Criando os campos
    titulo: {
        type: Sequelize.STRING,
        allowNull: false
    },
    descricao: {
        type: Sequelize.TEXT,
        allowNull: false
    }
})

//Sincroniza com o banco, force false, faz com que a tabela nao seja criada caso exista.
Pergunta.sync({force: false}).then(() => {});

module.exports = Pergunta;