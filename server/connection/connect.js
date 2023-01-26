
require('dotenv').config()
const mongoose = require('mongoose');
mongoose.set('strictQuery', true);
const connect = async()=>{
    try {
        await mongoose.connect('mongodb://localhost:27017/AuthUser', {
          useNewUrlParser: true,
          useUnifiedTopology: true
      });
        console.log("mongodb connected");
      } catch (error) {
        console.log(error);
      }
}
module.exports = connect