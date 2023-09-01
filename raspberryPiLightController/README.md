# Main raspberry pi controller code

This directory contains code for the raspberry pi that will control the lights. It will subscribe to PLS/1 on the local MQTT server and listen for new commands. It also checks for the state of a switch, so the lights can also be controlled with a physical button. 

## Wiring it up

To prepare the raspberry pi, you only need to wire up the button between pin 17 and GND. The relay module will need pins 27, VCC and GND. That's all you need to connect circuit-wise!

## Setting up the software

First of all: you need to install Raspberry Pi OS to the raspberry pi. After setting it up, just make a copy of button.py and mqtt.py in the directory you prefer (but keep that directory in mind). You can run the files directly to make sure they are running correctly, but for the day to day use, we'll prefer the code to run at startup.

To run the code, we will use a tool called tmux. It allows you to run whatever command you want in the background, and check on it from anywhere! If you don't have it installed, its simplt to get it:  `sudo apt install tmux`

After that, run  `crontab -e`  and add these lines to the end of the file:

    @reboot tmux new-session -d -s "mqttSub" "python3 /home/pi/mqtt.py"
    @reboot tmux new-session -d -s "button" "python3 /home/pi/button.py"

Remember! If you put the files on a different location, you'll need to change this part!

After that, just save the file and restart the raspberry pi. If everything goes right, you should see 2 sessions open on tmux when it reboots:

    pi@LeLights:~/ # tmux ls
    button: 1 windows (created Sat Aug 26 05:36:02 2023) [80x24]
    mqttSub: 1 windows (created Fri Sep  1 00:54:23 2023) [80x24]

Try sending an mqtt packet and see if the lights turn on!