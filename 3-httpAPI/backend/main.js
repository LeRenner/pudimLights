
const express = require('express')
const app = express()
const port = 3000

var mqtt = require('mqtt');

// read mqtt broker address from /config/hostname
var hostname = require('fs').readFileSync('/config/hostname', 'utf-8').trim();

// read mqtt broker port from /config/port
var mqttPort = require('fs').readFileSync('/config/port', 'utf-8').trim();

//connect 
var client = mqtt.connect('mqtt://' + hostname + ':' + mqttPort);

console.log(client)

app.get('/1/on', (req, res) => {
  console.log("/1/on")
  client.publish("PLS/1", "1");
  res.send('Sucess!');
})

app.get('/1/off', (req, res) => {
  console.log("/1/off")
  client.publish("PLS/1", "0");
  res.send('Sucess!');
})

app.get('/2/on', (req, res) => {
  console.log("/2/on")
  client.publish("PLS/2", "1");
  res.send('Sucess!');
})

app.get('/2/off', (req, res) => {
  console.log("/2/off")
  client.publish("PLS/2", "0");
  res.send('Sucess!');
})


app.listen(port, () => {
  console.log(`Application listening on port ${port}`)
})
