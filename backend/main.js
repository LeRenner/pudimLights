
const express = require('express')
const app = express()
const port = 3000

var mqtt = require('mqtt');
var client = mqtt.connect("mqtt://mosquitto");
console.log(client)

app.get('/1/on', (req, res) => {
  console.log("/1/on")
  client.publish("PLS/abajour", "1");
  res.send('Sucess!');
})

app.get('/1/off', (req, res) => {
  console.log("/1/off")
  client.publish("PLS/abajour", "0");
  res.send('Sucess!');
})

app.get('/2/on', (req, res) => {
  console.log("/2/on")
  client.publish("PLS/mesa", "1");
  res.send('Sucess!');
})

app.get('/2/off', (req, res) => {
  console.log("/2/off")
  client.publish("PLS/mesa", "0");
  res.send('Sucess!');
})


app.listen(port, () => {
  console.log(`Application listening on port ${port}`)
})
