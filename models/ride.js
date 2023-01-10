const mongoose = require('mongoose')

const schema = new mongoose.Schema({

    username: {
        type: String,
        required: true,
        min: 3,
        max: 20,
    },
    fromPlace: {
        type: String,
        require:true
    },
    toPlace: {
        type:String,
        required:true
    },
    rideDate: {
        type: String,
        require:true
    },
    rideTime: {
        type: String,
        required:true
    },
    availableSeat:{
        type:Number,
        required:true
    }
})

module.exports = mongoose.model("Rides",schema)