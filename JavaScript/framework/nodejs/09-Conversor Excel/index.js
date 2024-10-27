const fs = require("fs");

//Leitor de arquivos
fs.readFile("./usuario.json", {encoding: 'utf-8'},(erro, dados) => {

    if(erro){
        console.log('Deu ruim')
    }else{
        conteudo = JSON.parse(dados);
        conteudo.curso = 'Teste'
        console.log(conteudo)

        fs.writeFile("./usuario.json", JSON.stringify(conteudo), (err) => {
            if (err){
                console.log('Erro')
            }
        })

    }

})

//Escritor
fs.writeFile("./teste.txt", 'Texto que será adicionado', (err) => {

    if (err){
        console.log('Erro')
    }
})
