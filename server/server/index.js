const express = require('express')
const router = require('../router/index')

const app = express()

app.use('/', router)
app.get('/', async(req,res) =>{
    try {
        res.status(200).send({message:'working fine all thing in order 🍔🍔🍔🍔'})
    } catch (error) {
        res.status(404).send({error})
    }
})

module.exports = app