
function enviarEmail(corpo, para){

    return new Promise((resolve, reject) => {
        setTimeout(() => {

            var deuErro = false
            

            if(!deuErro){
                resolve({time: 6, to: "pedropanosso"})
            } else {
                reject("Fila cheia")
            }

        }, 1000)
    })

}

//Como o retorno de uma funcao é um objeto do tipo promise, ele tem 2 tipos de retorno:
//Caso a promessa de certo e caso de errado
//para isso são necessárias as 2 funções, resolve e reject. Onde cada uma é chamada quando a função der certo e errado respectivamente.
//Para serem acessadas utilizamos o operados then para o resolve e catch para o reject

enviarEmail('Ola Mundo', 'pedropanosso@gmail.com').then(({time, to}) => {
    console.log("Opa, deu certo " + to);
    
}).catch((err) => {
    console.log('Deu erro irmao: ' + err);
    
})

async function pegarId(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            
            resolve(5)

        }, 2000);
    })
}


async function buscarEmail(id){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve("pedropanopsso@gmail.com")
        }, 2000);
    })
}

// promises aninhadas

// pegarId().then((id) => {
//     buscarEmail(id).then((email) => {
//         enviarEmail('Ola MUndo', email).then(() => {
//             console.log("Enviar e-mail para o usuário " + id);
            
//         }).catch()
//     }).catch()
// }).catch()


function pegarUsuario(){
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            
            resolve([
                {name: "Pedro", lag: "Python"},
                {name: "Gabriel", lag: "JS"},
                {name: "Ana", lag: "C#"}
            ])            

        }, 3000);
    })
}

//Funcao async nos permite usar o await
async function principal(){
    
    //Aviso ao JS que eu quero que a promise seja concluida para ele pegar o resultado
    try{

        //Será executado esse bloco de código, caso ocorra algum erro, será enviado diretamente para o catch.
        var id = await pegarId();
        var email = await buscarEmail(id);
        enviarEmail('Teste', email)

    }catch(erro) {
        console.log(erro);
        
    }
    
}

principal()
