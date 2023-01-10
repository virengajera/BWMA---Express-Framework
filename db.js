const mongoose = require('mongoose')
const path = require('path')


mongoose.connect('mongodb://127.0.0.1:27017/bwma',{
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }).then(()=>{

    console.log('DB connected sucessfully')
  }).catch((err)=>{

    console.error(err.message)
  })