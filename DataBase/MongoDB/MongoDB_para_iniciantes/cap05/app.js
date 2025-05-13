const { MongoClient, ObjectId } = require ("mongodb") ;
const express = require("express")
const app = express()
const port = 3000
const router = express.Router();

async function connect () {

    if ( global.db ) 
        return global.db;
    
    const client = new MongoClient("mongodb://127.0.0.1:27017/") ;
    await client.connect();
    global.db = await client.db("workshop") ;
    return global.db;
}

app.use(express.json())

app.get('/', (req, res) => res.json({message: 'Funcionando'}))

router.get('/clientes', async(req, res, next) => {
    try {
        const db = await connect();
        res.json(await db.collection("customer").find().toArray())
    }
    catch (ex) {
        console.log(ex)
        res.status(400).json({erro: `${ex}`})
    }
})

router.get('/clientes/:id', async(req, res, next) => {
    try{
        const db = await connect();
        if (req.params.id){
            res.json(await db.collection("customer").findOne({_id: new ObjectId(req.params.id)}));
        } else {
            res.join(await db.collection("customer").find().toArray())
        }
    }
    catch (ex) {
        console.log(ex)
        res.status(400).json({err: `${ex}`})
    }
})

router.post('/clientes/', async(req, res, next) => {
    try{
        const db = await connect()
        const customer = req.body;
        res.json( await db.collection("customer").insertOne(customer))
        
    }
    catch (ex) {
        console.log(ex)
        res.status(400).json({err: `${ex}`})
    }
})

router.put('/clientes/:id', async(req, res, next) => {
    try{
        const db = await connect()
        const customer = req.body;
        const id = {_id: new ObjectId(req.params.id)};
        console.log(id)
        if (id) {
            res.json( await db.collection("customer").updateOne(id, { $set: customer}))
        }
        
        
    }
    catch (ex) {
        console.log(ex)
        res.status(400).json({err: `${ex}`})
    }
})

router.delete('/clientes/:id', async(req, res, next) => {
    try{
        const db = await connect()
        const customer = req.body;
        const id = {_id: new ObjectId(req.params.id)};
        if (id) {
            res.json( await db.collection("customer").deleteOne(id, { $set: customer}))
        }
        
        
    }
    catch (ex) {
        console.log(ex)
        res.status(400).json({err: `${ex}`})
    }
})

app.use('/', router)

app.listen(port)

console.log('API Funcionando!')