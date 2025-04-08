import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
client.client_id = "Remote_Graph" 

client.connect(mqttBroker)
i = 0
while True:
    client.publish("Elephant_cx_cy", str(i))
    print(f"Published {i}")
    i += 1
    time.sleep(3)
