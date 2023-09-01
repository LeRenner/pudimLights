# Pudim Lights

This repository documents the DIY smart lights I set up in my room, and the system behind them. Feel free to replicate this project yourself, but remember: playing with mains voltage is dangerous, and you should always talk to an electrician if you are going to modify any equipment that plugs into the wall!

![Demonstration gif](./demonstration.gif)

## How it works

I wanted to be able to turn on my room lights both with a physical switch and with any program that I wanted to integrate with it. I decided to use MQTT for the communication on my local network because it is simple, lightweight and perfect for this kind of application. This way, to turn ON or OFF any of the lights, you just need to send an MQTT packet to the broker (or, even fancier, an HTTP request!).

To make the lights controllable from outside my home, I also wrote a little program that receives HTTP requests and sends MQTT packets to my local broker, so even my friends can control my lights with a little website! (yes, this is an objetively dumb idea!)

This repository contains 3 pieces of code: the HTTP API that sends MQTT packets to the broker, and subsequently to the controllers, and two light controllers: one for the raspberry pi and other for the esp32. Check out their directories to see how to upload the code and get it running!

## Turning ON and OFF the lights

After setting up any of the controllers, just send a publish request to the MQTT broker with the topic `PLS/1` or `PLS/2` with contents `0` to turn it OFF, and `1` to turn it ON. If you have the API set up and configured, you can also send a GET request to `/1/on` to turn the light 1 ON, of example.

## Setting it up yourself

To set up the light controllers, just enter the directories above and check out the READMEs. They explain how to upload and get the code running. You'll also need an MQTT broker. Mine runs inside my kubernetes cluster at my home. Here's my [deployment](https://github.com/LeRenner/pudimnetes/blob/main/configFiles/11-mosquitto.yml) if you are curious. In that repository there's also the [HTTP API deployment](https://github.com/LeRenner/pudimnetes/blob/main/configFiles/07-plsBackend.yml), if you want to check it out!