const db = require('../db')
const Rides = require('../models/ride')

console.log(Rides)

function offerRide(req, res) {
    try {

        const { username, fromPlace, toPlace, rideDate, rideTime, availableSeat } = req.body

        console.log(req.body)

        let newRide = new Rides({
            username,
            fromPlace,
            toPlace,
            rideDate,
            rideTime,
            availableSeat
        })
        console.log(newRide)
        newRide.save((err, newRide) => {
            console.log('--------------------------------------------------->')

            if (err) {
                res.send(err)
            } else {
                res.send({ "message": "ride is sucessfully added", newRide })
            }
        })

    }
    catch (error) {
        res.json(error)
    }
}

async function searchRide(req, res, next) {
    const from = req.query.from
    const to = req.query.to

    req.params.id

    try {


        const result = await Rides.find({

            $and: [
                { "fromPlace": { $eq: from } },
                { "toPlace": { $eq: to } }
               
            ]

        })

        res.send(result)

    }
    catch (err) {
        res.json(err)
    }
}

module.exports.offerRide = offerRide
module.exports.searchRide = searchRide