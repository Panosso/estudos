const express = require('express')
const router = express.Router()
const rotas = require('./rotasArticles.js')

router.get('/', rotas.artigoRoot)
router.get('/cadastro', rotas.artigoCadastro)
router.get('/editar/:id_art', rotas.artigoEditar)
router.get('/page/:num', rotas.artigoPag)

router.post('/save', rotas.artigoSave)
router.post('/delete', rotas.artigoDelete)



module.exports = router;
