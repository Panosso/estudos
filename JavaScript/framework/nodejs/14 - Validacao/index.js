var express = require("express");
var app = express();
var session = require("express-session");

//Usado para ser usada apenas uma vez, e então a sessão é expiradas
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

    var emailError = req.flash("emailError")
    var pontosError = req.flash("pontosError")
    var nomeError = req.flash("nomeError")
    var email = req.flash("email")

    emailError = (emailError == undefined || emailError.lenght == 0 ) ? undefined : emailError
    pontosError = (pontosError == undefined || pontosError.lenght == 0 ) ? undefined : pontosError
    nomeError = (nomeError == undefined || nomeError.lenght == 0 ) ? undefined : nomeError
    email = (email == undefined || email.lenght == 0 ) ? "" : email

    console.log(email)

    res.render("index", {emailError, pontosError, nomeError, email: email })
})

app.post("/form", (req, res) => {

    var {email, nome, pontos} = req.body
    
    var emailError
    var pontosError
    var nomeError

    if (email == undefined || email == ""){
        emailError = "Email invalido"
    }

    if (pontos == undefined || pontos < 20) {
        pontosError = "Pontos Invalidos"
    }

    if (nome == undefined || nome == "") {
        nomeError = "nome invalido"
    }

    if (emailError != undefined || pontosError != undefined || nomeError != undefined){
        req.flash("emailError", emailError)
        req.flash("pontosError", pontosError)
        req.flash("nomeError", nomeError)
        req.flash("email", email)
        res.redirect("/")
    }else{
        res.send("Show de bola")
    }

})

app.listen(5678,(req, res) => {
    console.log("Servidor rodando!");
});