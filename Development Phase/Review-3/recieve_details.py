import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("Elephant_cx_cy")

def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic {msg.topic}")

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)


client.on_connect = on_connect
client.on_message = on_message


client.connect(mqttBroker)
client.loop_forever() 