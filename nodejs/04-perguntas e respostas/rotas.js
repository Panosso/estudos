function raiz(req, res){

    // O Express ja entende que a pasta views que está no mesmo nível do projeto, tem os arquivos, não é necessário informar a extensão do arquivo

    const nome = req.params.nome
    const lenght = req.params.lenght
    var exibirMsg = false
    var prod = [
        {nome: "Doritos", preco: 3.14},
        {nome: "Coca-Cola", preco: 2.14},
        {nome: "Leite", preco: 1.14}
    ]

    res.render("html/index.ejs", {
        nome: nome,
        lenght: lenght,
        msg: exibirMsg,
        produtos: prod
    })

}

function home(req, res){

    res.render("html/home")

}

function perguntar(req, res){

    res.render("html/perguntar")
}

module.exports = {
    raiz,
    home,
    perguntar
}