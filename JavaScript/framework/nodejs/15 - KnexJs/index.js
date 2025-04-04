var database = require("./database")

var dados = [{
        nome: "Killer instinct 3",
        preco: 120
    },

    {   nome: "COD",
        preco: 10},

    {   nome: "Final Fantasy",
        preco: 20},

    {   nome: "Driver 2",
        preco: 1120}

]

//Insert
// database.insert(dados).into('games').then(data => {
//                                             console.log(data)
//                                         }).catch(err => {
//                                             console.log(err)
//                                         })

// database.select().table("games").then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })


// database.select(['preco', 'nome'])
//             .table("games")
//             .where({nome: "Killer instinct"})
//             .orWhere({id: 8}).then(data => {
//                     console.log(data)
//                 }).catch(err => {
//                     console.log(err)
//                 })


// //WhereRaw --> Equivalente ao Like em sql --> 
// database.select(['preco', 'nome'])
//             .table("games")
//             .whereRaw("nome like 'Killer insti%'").then(data => {
//                     console.log(data)
//                 }).catch(err => {
//                     console.log(err)
//                 })


// //SQL puro usando o raw
// database.raw("select * from games;")

// //delete
// database.where({id: 8}).delete().table('games').then(data => {
//     console.log(data + " Deletei")
// }).catch(err => {
//     console.log(err)
// })

// //update
// database.where({id: 7}).table('games').update({nome: 'Wow'}).then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// //order by

// database.select().table('games').orderBy("preco", "asc").then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

async function teste_transacao() {

    try{

        //callback com funcao assincrona
        await database.transaction(async trans => {
            await database.insert(dados).into('games')
        })

    }catch(err){
        console.log(err)
    }

}

teste_transacao()