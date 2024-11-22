const express = require('express')
const jwt = require('jsonwebtoken')

const app = express()

const port = 4000

app.get('/api/token', (req, res) => {
    const payload = {
        name: 'Pedro'
    }

    const secret = "teste1234"

    const token = jwt.sign(payload, secret, {
        expiresIn: '1h'
    })

    res.status(200).json({
        token
    })
})

app.get('/api/verify', (req, res) => {
    const token = req.headers['authorization']?.split(' ')[1] || '';
    const secret = "teste1234"

    try {
        const decoded = jwt.verify(token, secret)
        res.status(200).json({
            data: decoded
        })
    }catch(error){
        res.status(401).json({
            message: 'Invalid token'
        })
    }
})

app.listen(port)