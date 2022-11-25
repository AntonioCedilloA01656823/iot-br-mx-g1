const mqtt = require('mqtt')
const mysql = require('mysql')

const db = mysql.createConnection({
    host: "localhost",
    port: 3306,
    user: 'root',
    password: 'T0n1tO#313', // Change with ur sql database and port data
    database: 'events'
})

db.connect(() => {
    console.log('Database ok!')
})

const sub = mqtt.connect('mqtt://localhost:9000')

sub.on('connect', () => {
    console.log('Connected to mqtt broker')
    sub.subscribe('test')
})

sub.on('message', (topic, message) => {
    console.log("message read")
    let m = JSON.parse(message)
    console.log("color: " + m.color + ", lat: " + m.lat + ", lon: " + m.lon)
    db.query(
        'insert into events set ?',
        {lat: m.lat, lon: m.lon, color: m.color},
        (err, rows) => {
            if(!err) console.log('data saved!')
        }
    )
})
