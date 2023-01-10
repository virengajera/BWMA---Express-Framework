const express = require('express')
const app = express()
const rideRouter = require('./routes/ride')
const bodyParser = require('body-parser')


app.use(bodyParser.json())

app.use('/api',rideRouter)

app.listen(3000,(err)=>{

    console.log('App is running on 3000')
})