const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors")
const jwt = require("jsonwebtoken")

const JWTSecret = "uohohdsohudsahodasohdpahgupsihgaiuoshgiosadh"

app.use(bodyParser.urlencoded({extended: false}));
app.use(bodyParser.json());
app.use(cors())

//Middleware: Uma função que é executada antes da requisição enviada pelo usuário.
function authMiddle(req, res, next){

    const authToken = req.headers['authorization']

    if (authToken != undefined){
        const bearer = authToken.split(" ")
        var token = bearer[1]

        jwt.verify(token, JWTSecret, (err, data) => {
            if (err){
                res.status(401)
                res.json({err: "Token inválido"})
            }else{

                //Adiciona essas variáveis na requisição, sendo possível recupera-las na rota
                req.token = token
                req.loggedUser = {id: data.id, email: data.email}


                //Funcão responsável por passar a requisição do middleware para a rota desejada
                next()
            }
        })

    }else{
        res.status(401)
        res.json({err: "Token Inválido"})
    }


}

var DB = {
    games: [
        {
            id: 23,
            title: "Call of duty MW",
            year: 2019,
            price: 60
        },
        {
            id: 65,
            title: "Sea of thieves",
            year: 2018,
            price: 40
        },
        {
            id: 2,
            title: "Minecraft",
            year: 2012,
            price: 20
        }
    ],
    users : [
        {
            id: 1, 
            nome: "Pedro",
            email: "pedro@pedro.com.br",
            passwd: "123321123321"
        },

        {
            id: 2, 
            nome: "Pedro2",
            email: "pedro2@pedro2.com.br",
            passwd: "asddsaasddsa"
        }

    ]
}

app.post("/auth", (req, res) =>{

    var {email, passwd} = req.body;

    if (email != undefined){

        //Verifica se o e-mail existe no banco
        var user = DB.users.find(user => user.email == email)

        if (user != undefined){

            if (user.passwd == passwd) {

                jwt.sign({id: user.id, email: user.email}, 
                        JWTSecret,
                        {expiresIn:'48h'},
                        (err, token) => {
                            if(err){
                                res.status(400)
                                res.json({err: "Falha interna"})
                            }else{
                                res.status(200)
                                res.json({token: token})
                            }
                })

            }else{
                res.status(401);
                res.json({err: "Não autorizado"})
            }

        }else{
            res.status(404);
            res.json({err: "O e-mail não existe na base de dados"})
        }

    }else {
        res.status(400);
        res.json({err: "O e-mail está invalido"})
    }


})

app.get("/games", authMiddle, (req, res) => {

    //Recuperando as variaveis criadas no middleware
    console.log(req.loggedUser)
    res.statusCode = 200;
    res.json(DB.games);
});

app.get("/game/:id",(req, res) => {
    
    if(isNaN(req.params.id)){
        res.sendStatus(400);
    }else{
    
        var id = parseInt(req.params.id);

        HATEOAS = [
            {
                href: "http://localhost:45678/game/" + id,
                method: "GET",
                rel: "get_game"
            },
            {
                href: "http://localhost:45678/game/" + id,
                method: "DELETE",
                rel: "delete_game"
            },
            {
                href: "http://localhost:45678/auth",
                method: "POST",
                rel: "login"
            }            
        ]


        var game = DB.games.find(g => g.id == id);

        if(game != undefined){
            res.statusCode = 200;
            res.json({game: game, _link: HATEOAS});
        }else{
            res.sendStatus(404);
        }
    }
});

app.post("/game",(req, res) => { 
    var {title, price, year} = req.body;
    DB.games.push({
        id: 2323,
        title,
        price,
        year
    });
    res.sendStatus(200);
})

app.delete("/game/:id",(req, res) => {
    
    if(isNaN(req.params.id)){
        res.sendStatus(400);
    }else{
        var id = parseInt(req.params.id);
        var index = DB.games.findIndex(g => g.id == id);

        if(index == -1){
            res.sendStatus(404);
        }else{
            DB.games.splice(index,1);
            res.sendStatus(200);
        }
    }
});

app.put("/game/:id",(req, res) => {

    if(isNaN(req.params.id)){
        res.sendStatus(400);
    }else{
        
        var id = parseInt(req.params.id);

        var game = DB.games.find(g => g.id == id);

        if(game != undefined){

            var {title, price, year} = req.body;

            
            if(title != undefined){
                game.title = title;
            }

            if(price != undefined){
                game.price = price;
            }

            if(year != undefined){
                game.year = year;
            }
            
            res.sendStatus(200);

        }else{
            res.sendStatus(404);
        }
    }

});

app.listen(45678,() => {
    console.log("API RODANDO!");
});