const router = require('express').Router()

const rideCtrl = require('../controller/ride')

router.post('/offerRide',rideCtrl.offerRide)

router.get('/searchRide/:id',rideCtrl.searchRide)

module.exports = router