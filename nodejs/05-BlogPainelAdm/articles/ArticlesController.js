const express = require('express')
const router = express.Router()
const rotas = require('./rotasArticles.js')

router.get('/', rotas.artigoRoot)
router.get('/cadastro', rotas.artigoCadastro)
router.get('/editar/:id_cat', rotas.artigoEditar)

router.post('/save', rotas.artigoSave)
router.post('/delete', rotas.artigoDelete)



module.exports = router;
