#!/usr/bin/python3

buttonPin = 17
lightPin = 27

import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lightPin, GPIO.OUT)

# Main variables
buttonState = GPIO.input(buttonPin)
previousButtonState = buttonState
cons = 0
lightState = 0

# Main loop
#
# Extra logic is added for debouncing the button
while True:
    # Get current button state
    buttonState = GPIO.input(buttonPin)

    # If the button is still pressed, increment the counter
    if previousButtonState == 1 and buttonState == 1: cons += 1
    
    # If the button is not pressed, reset the counter
    if buttonState == 0: cons = 0

    # If the counter reaches 30, toggle the light
    if cons == 30:
        lightState = not lightState
        GPIO.output(lightPin, lightState)

    # Set the previous button state
    previousButtonState = buttonState
    time.sleep(0.001)