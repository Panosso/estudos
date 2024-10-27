
//O set timeout é assincrono, ou seja, ele fica executando enquanto o sistema continua as instruções
function enviarEmail(corpo, para, callback){
    setTimeout(() => {
        console.log(`Para: ${para}
            -----------------
            ${corpo}
            -----------------
            De: Vitor Lima`
        );


        //...Logica

        var deuErro = true;

        if(deuErro){

            callback("O envio falhou")

        }else{

            //A função callback pode receber parametros mesmo que não declardos
            callback();

        }


    }, 8000)

}

console.log('Inicio do envio de e-mail')

enviarEmail("Ola seja bem vindo", "pedropanosso@gmail.com", (erro) => {
    if (erro == undefined){
        console.log('Tudo Ok');        
    }else {
        console.log("Ocorreu um erro: " + erro );
        
    }
        
})

console.log('Fim do envio de e-mail')
