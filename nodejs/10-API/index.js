const express = require("express")
const app = express()
const bodyParser = require("body-parser");
const { log } = require("console");

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());

var DB = {
    games: [
        {
            id: 1,
            title: 'Call',
            year: 2020,
            price: 50
        },
        {
            id: 2,
            title: 'mine',
            year: 2010,
            price: 520
        },
        {
            id: 3,
            title: 'bee',
            year: 2019,
            price: 5
        }
    ]
}

app.get("/games", (req, res) =>{
    res.statusCode = 200
    res.json(DB.games)
})

app.get("/game/:id", (req, res) => {
    if(isNaN(req.params.id)){
        res.sendStatus(400);
    }else{
        var id = req.params.id

        var game = DB.games.find(g => g.id == id);

        if(game != undefined){
            res.statusCode = 200;
            res.json(game)
        }else{
            res.sendStatus(404)
        }
    }

})

app.post("/game", (req, res) => {

    var {title, price, year} = req.body;

    DB.games.push({
        id: 123,
        title,
        price,
        year
    });

    res.sendStatus(200)
    

})

app.delete("/game/:id", (req, res) => {
    if(isNaN(req.params.id)){
        res.sendStatus(400);
    }else{
        var id = req.params.id
        var game = DB.games.findIndex(g => g.id == id)

        if(game == -1){
            res.statusCode(404)
        }else{
            DB.games.splice(game, 1)
            res.sendStatus(200)
        }

    }
})

app.listen(1234,() => {
    console.log('Rodando');
    
})