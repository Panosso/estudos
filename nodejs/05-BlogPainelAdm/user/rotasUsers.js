const { Model, where } = require("sequelize")
const User = require("./User")
const slugify = require('slugify')
const bcrypt = require('bcryptjs')
const adminAuth = require('../middleware/adminAuth')

function userRoot(req, res){

    User.findAll().then(users => {

        res.render('admin/users/index', {users: users})

    })
}

function userCreate(req, res){
    res.render('admin/users/create')
}

function userSave(req, res){
    var email = req.body.email;
    var password = req.body.password;

    User.findOne({

        where: {email: email}

    }).then( user => {

        if (user == undefined){

            var salt = bcrypt.genSaltSync(10)
            var hash = bcrypt.hashSync(password, salt)
        
            User.create({
                email: email, 
                password: hash
            }).then(() => {
                res.redirect("/usuarios/")
            }).catch((err) => {
                res.redirect("/usuarios/")
            })

        }else{

            res.redirect('/usuarios/create')

        }

    })
}

function userLogin(req, res){
    res.render('admin/users/login')
}

function userLogar(req, res){

    var email = req.body.email;
    var password = req.body.password;

    User.findOne({
        where: {email: email}
    }).then(user => {
        if(user != undefined){

            var correct = bcrypt.compareSync(password, user.password)

            if (correct){
                req.session.user = {
                    id: user.id,
                    email: user.email
                }

                res.json(req.session.user)

            }else{

                res.redirect("/usuarios/login")
            }

        }else{
            res.redirect("/usuarios/login")
        }
    })

}

function userLogout(req, res){
    req.session.user = undefined
    res.redirect("/")
}

module.exports = {
    userRoot,
    userCreate,
    userSave,
    userLogin,
    userLogar,
    userLogout
}