const { where } = require('sequelize')
const Pergunta = require('./database/Pergunta.js')
const Respostas = require('./database/Respostas.js')


function raiz(req, res){

    // O Express ja entende que a pasta views que está no mesmo nível do projeto, tem os arquivos, não é necessário informar a extensão do arquivo

    // const nome = req.params.nome
    // const lenght = req.params.lenght
    // var exibirMsg = false
    // var prod = [
    //     {nome: "Doritos", preco: 3.14},
    //     {nome: "Coca-Cola", preco: 2.14},
    //     {nome: "Leite", preco: 1.14}
    // ]

    // res.render("html/index.ejs", {
    //     nome: nome,
    //     lenght: lenght,
    //     msg: exibirMsg,
    //     produtos: prod
    // })

    Pergunta.findAll({raw: true, 
                      order:[['id', 'ASC']]})
        .then(perguntas => {
            res.render("html/index.ejs", {
                perguntas: perguntas
            })
        })

}

function home(req, res){

    res.render("html/home")

}

function perguntar(req, res){

    res.render("html/perguntar")
}

function salvarpergunta(req, res){

    var titulo = req.body.titulo;
    var descricao = req.body.descricao;
    
    Pergunta.create({
        titulo: titulo,
        descricao: descricao
    }).then(() => {
        res.redirect("/")
    })

}

function pergunta(req, res){
    var id = req.params.id;

    Pergunta.findOne({
        where: {id: id}
    }).then(pergunta => {
        if(pergunta != undefined){

            Respostas.findAll({
                where: {perguntaId: id},
                order: [['id', 'DESC']]
            }).then(respostas => {
                    res.render('html/pergunta', {
                        pergunta: pergunta,
                        respostas: respostas
                    })
                })

        }else{

            res.redirect("/")

        }

    })

}

function salvarresposta(req, res){

    const corpo = req.body.corpo
    console.log(corpo)
    const perguntaId = req.body.perguntaId
    console.log(perguntaId)

    Respostas.create({
        corpo: corpo,
        perguntaId: perguntaId
    }).then(() => {
        res.redirect('/pergunta/' + perguntaId)
    })

}

module.exports = {
    raiz,
    home,
    perguntar,
    salvarpergunta,
    pergunta,
    salvarresposta
}