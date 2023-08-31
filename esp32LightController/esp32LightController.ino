#include <WiFi.h>
#include <PubSubClient.h>

#define buttonPin 13
#define lightPin 27

int lightState = 1;

const char* ssid = "LeFastWifi";
const char* password = "XXXXXXXXXXXXXX";
const char* mqtt_server = "192.168.15.120";
const int mqtt_port = 32032;
const char* lightTopic = "PLS/2";

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
	Serial.begin(115200);
	Serial.println("Hello, world!");
	delay(2000);

	pinMode(lightPin, OUTPUT);
	pinMode(buttonPin, INPUT_PULLUP);
	digitalWrite(lightPin, lightState);

	WiFi.begin(ssid, password);

	while (WiFi.status() != WL_CONNECTED) {
		delay(500);
		Serial.print(".");
	}

	Serial.println("WiFi connected");

	client.setServer(mqtt_server, mqtt_port);
	client.setCallback(callback);
}

void callback(char* topic, byte* message, unsigned int length) {
	if (length < 1) return;

	Serial.print("New message! Contents ->");
	Serial.print(topic);
	Serial.print("|| Message ->");
	Serial.println(message[0]);

	if (length == 1) {
		if (String(topic) == lightTopic) {
			if (message[0] == '0') {
				digitalWrite(lightPin, 1);
				lightState = 1;
			}
			else if (message[0] == '1') {
				digitalWrite(lightPin, 0);
				lightState = 0;
			}
		}
	}
}

void reconnect() {
	while (!client.connected()) {
		Serial.print("Attempting MQTT connection...");
		if (client.connect("ESP8266Client")) {
			Serial.println("connected");
			client.subscribe(lightTopic);
		} else {
			Serial.print("failed, rc=");
			Serial.print(client.state());
			Serial.println(" try again in 5 seconds");
			delay(5000);
		}
	}
}

void loop() {
	if (!client.connected()) {
		reconnect();
	}

	client.loop();

	int buttonReading = digitalRead(buttonPin);

	if (buttonReading == LOW && lightState == 0 || buttonReading == HIGH && lightState == 1) {
		digitalWrite(lightPin, lightState);
		lightState = !lightState;
	}
}
