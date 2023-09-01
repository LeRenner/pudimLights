# Part 3: HTTP API

After parts 1 and 2, I was able to send MQTT packets to turn on and off my lights. This is cool, but not very convenient. In order to make ir much more simpler to integrate with other programs and automations, I wanted to open a public API so that I (as well as anyone on the internet) is able to turn on my lights.

Is is a simple docker container. It opens on port 3000 and receives requests on `/lightNumber/state`, so `/1/on` turns light 1 on, for example. You can route that container however you want. I originally routed it through a Caddy proxy for HTTPS before exposing it to the internet. Nowadays, it is simply part of my k8s cluster. I'm not going to say directly what is the link to turn on my lights, but if you look a little bit closer (at my kubernetes repository) you'll be able to quickly figure it out.

In adition to the files to build the docker container, this directory also has the k8s deployment for my service, as well as my old docker-container.yml deployment in case you want to check it out.