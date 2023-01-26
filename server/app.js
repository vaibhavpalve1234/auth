const express = require('express');
const server = require('./server/index')
const connect = require('./connection/connect');
const bodyParser = require('body-parser');
require('dotenv').config()

const app =  express()

app.use(bodyParser.json())
app.use('/',server)

app.listen(8080, async(req,res) =>{
    await connect()
    console.log(`server started ad ${8080}  please check apis working conditions`);
})

