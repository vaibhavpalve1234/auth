const express = require('express')
const { getUserDetails,createRegisterUser,updateRegisterUser,deleteRegisterUser, getLoginDetails,postLoginDetails,updateLoginDetails, deleteLoginDetails } = require('./authRouter')

const router = express.Router()
    .get('/register', getUserDetails)
    .post('/register', createRegisterUser)
    .put('/register', updateRegisterUser)
    .delete('/register', deleteRegisterUser)

    .get('/login', getLoginDetails)
    .post('/login', postLoginDetails)
    .put('/login', updateLoginDetails)
    .delete('/login', deleteLoginDetails)

module.exports = router