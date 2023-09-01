# Main esp32 controller code

This directory contains code for the esp32 that will control the lights. It will subscribe to PLS/2 on the local MQTT server and listen for new commands. It also checks for the state of a switch, so the lights can also be controlled with a physical button. 

## Wiring it up

To prepare the esp32, you only need to wire up the button between pin 13 and GND. The relay module will need pins 27, VCC and GND. That's all you need to make this controller!

## Programming it

First of all, you'll need to edit a little bit of code! In esp32LightController.ino, you'll need to set the correct hostname and port for the mqtt server, as well as your wifi credentials. You can also customize the topic the esp32 will listen to.

I recommend arduino-cli to flash code on microcontrollers. If you have arduino-cli installed, all you need to do is run the preinstall, which will install some needed libraries and platforms, and then run `make upload` to send the code to the board. Make sure to check if your board is on the same TTY as mine (its in the makefile)!

If you prefer to use another programmer, you simply need to flash esp32LightController.ino to the esp32 board!

## Testing

Send manually a message to your mqtt broker and check if the relay clicks! If not, check the serial connection and see if your esp was able to connect to wifi and to the mqtt broker.