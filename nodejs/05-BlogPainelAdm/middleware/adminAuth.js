function adminAuth(req, res, next){

    if (req.session.user != undefined){
        
        //Nesse next serve para passar a requisição do middleware para a rota
        next();

    } else {
        res.redirect("/")
    }
}

module.exports = adminAuth