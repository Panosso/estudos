const express = require('express')
const router = express.Router();
const User = require('./User')


const rotas = require('./rotasUsers')
const adminAuth = require('../middleware/adminAuth')


//Admin auth veriofica se o usuário está logado, caso esteja ele ia acessar a rota, caso não ele não vai acessar e será redirecionado para a rota do adminAuth
router.get("/", adminAuth, rotas.userRoot)
router.get("/create", rotas.userCreate)
router.get("/login", rotas.userLogin)
router.get("/logout", rotas.userLogout)

router.post('/save', rotas.userSave)
router.post('/autenticar', rotas.userLogar)


module.exports = router;