function raiz(req, res){
    res.send("Bem vindo ao trem aqui <3") // A resposta só pode ser enviada uma vez por rota
    console.log('Estou na raiz')
}

function blog(req, res){
    var artigo = req.params.artigo
    var resposta

    if (artigo) {
        resposta = `Bem vindo ao bloger sobre o artigo: ${artigo}<br><br>
             <a href="http://localhost:4000/canal">Canal</a>`
    } else {

        resposta = `Faltou o artigo né amigo?`

    }

    res.send(resposta)
}

function canal(req, res){
    res.send('<h1>Bem vindo ao canal</h1>')
}

function youtube(req, res){
    //Essa variavel será preenchida caso seja passado um valor na url chamado canal
    //Ex: http://localhost:4000/youtube?canal=teste
    var canal = req.query['canal'];

    if (canal){
        res.send(`Canal selecionado: ${canal}`)
    } else {
        res.send('<h1>Bem vindo ao youtube, nenhum canal selecionado</h1>')
    }

}

function ola(req, res){

    var nome = req.params.nome
    var empresa = req.params.empresa

    res.send('Oi ' + nome + " vc trabalha em: " + empresa)

}

module.exports = {
    raiz,
    blog,
    canal,
    youtube,
    ola
}