//Usado para criar rotas
const express = require('express')
const router = express.Router()
const rotas = require('./rotasCategory.js')

router.get('/', rotas.categoriaRoot)
router.get('/cadastro', rotas.categoriaCadastro)
router.get('/editar/:id_cat', rotas.categoriaEditar)

router.post('/save', rotas.categoriesSave)
router.post('/delete', rotas.categoriesDelete)

module.exports = router;
