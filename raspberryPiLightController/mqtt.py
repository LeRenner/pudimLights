#!/usr/bin/python3

from paho.mqtt import client as mqtt_client
import RPi.GPIO as GPIO
import time

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, True)

# Main variables
pin = 17
broker = '192.168.15.120'
port = 32032
topic = "PLS/1"
client_id = "LeLights"


# Connects to MQTT broker
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


# Subscribes to MQTT topic
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        msg = msg.payload.decode()
        if msg == "1": GPIO.output(pin, False)
        if msg == "0": GPIO.output(pin, True)
    client.subscribe(topic)
    client.on_message = on_message


# Runs the MQTT client
def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()