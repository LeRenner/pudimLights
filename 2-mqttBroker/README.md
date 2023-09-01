# Part 2: MQTT Broker

The MQTT broker is the messenger of this whole project. It receives messages from anyone, and forwards them to anyone that want to listen to them. MQTT works in the publish/subscribe scheme. Users can substribe to how many topics they want. When someone publishes to a specific topic, all users subscribed to it receive the message.

I deliberately chose to disable login for my broker because 1) this system is no critical, and 2) it makes things much simpler for me.

Originally, the broker was set up on docker. However, since I migrated all my infrastructure to kubernetes, I ended up setting up an eclipse mosquitto deployment.

The file mosquitto.conf is mounted with the docker-compose.yml file.