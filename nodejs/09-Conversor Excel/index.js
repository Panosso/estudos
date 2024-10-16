const fs = require("fs");

fs.readFile("./teste.txt",{encoding: 'utf-8'},(erro, dados) => {

    if(erro){
        console.log('Deu ruim')
    }else{
        console.log(dados)
    }

})

