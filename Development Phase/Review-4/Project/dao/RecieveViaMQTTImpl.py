# Receiver class correction
import paho.mqtt.client as mqtt
import pickle
import threading

from datetime import datetime

from dao.RecieveViaMQTT import RecieveViaMQTT

class RecieveViaMQTTImpl(RecieveViaMQTT):
    def __init__(self):
        self.mqttBroker = "mqtt.eclipseprojects.io"
        self.line_chart_data = None
        self.subplot_data = None
        self.line_chart_ready = threading.Event()
        self.subplot_ready = threading.Event()
        
    def recieveForLineChart(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected for line chart data")
            client.subscribe("CXCYForLineChartTharun")

        def on_message(client, userdata, msg):
            try:
                self.line_chart_data = pickle.loads(msg.payload)
                self.line_chart_ready.set()
                print(f'Received at {datetime.now().strftime("%H:%M:%S")}')
            except Exception as e:
                print(f"Error processing line chart data: {e}")

        client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        client.on_connect = on_connect
        client.on_message = on_message

        try:
            client.connect(self.mqttBroker)
            client.loop_start()
            
            if self.line_chart_ready.wait(timeout=120):
                return self.line_chart_data
            else:
                print("Timeout waiting for line chart data")
                return None
                
        except Exception as e:
            print(f"Error in line chart receiver: {e}")
            return None
        finally:
            client.loop_stop()

    def recieveForSubPlot(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected for subplot data")
            client.subscribe("CXCYForSubPlotTharun")

        def on_message(client, userdata, msg):
            try:
                self.subplot_data = pickle.loads(msg.payload)
                self.subplot_ready.set()
                print("Received subplot data")
            except Exception as e:
                print(f"Error processing subplot data: {e}")

        client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        client.on_connect = on_connect
        client.on_message = on_message

        try:
            client.connect(self.mqttBroker)
            client.loop_start()
            
            if self.subplot_ready.wait(timeout=120):
                return self.subplot_data
            else:
                print("Timeout waiting for subplot data")
                return None
                
        except Exception as e:
            print(f"Error in subplot receiver: {e}")
            return None
        finally:
            client.loop_stop()