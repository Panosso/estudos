var express = require("express");
var app = express();
var session = require("express-session");
var flash = require("express-flash");
var bodyParser = require("body-parser");
var cookieParser = require("cookie-parser");

app.set('view engine','ejs');

app.use(bodyParser.urlencoded({ extended: false }))
 
app.use(bodyParser.json())

app.use(cookieParser("jsaddsh"));
app.use(session({
    secret: 'keyboard cat',
    resave: false,
    saveUninitialized: true,
    cookie: { maxAge: 60000 }
  }))

app.use(flash());

app.get("/", (req, res) => {
    res.render("index")
})

app.post("/form", (req, res) => {
    var {email, nome, pontos} = req.body
    
    if (email != undefined ){
        console.log("E-mail invalidos")
    }

})

app.listen(5678,(req, res) => {
    console.log("Servidor rodando!");
});