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
        self.line_client = None
        self.subplot_client = None
    
    def connect(self):
        # Set up persistent connections
        def on_line_connect(client, userdata, flags, rc):
            print("Connected for line chart data")
            client.subscribe("CXCYForLineChartTharun")

        def on_line_message(client, userdata, msg):
            try:
                self.line_chart_data = pickle.loads(msg.payload)
                self.line_chart_ready.set()
                print(f'Received line chart data at {datetime.now().strftime("%H:%M:%S")}')
            except Exception as e:
                print(f"Error processing line chart data: {e}")

        def on_subplot_connect(client, userdata, flags, rc):
            print("Connected for subplot data")
            client.subscribe("CXCYForSubPlotTharun")

        def on_subplot_message(client, userdata, msg):
            try:
                self.subplot_data = pickle.loads(msg.payload)
                self.subplot_ready.set()
                print(f'Received subplot data at {datetime.now().strftime("%H:%M:%S")}')
            except Exception as e:
                print(f"Error processing subplot data: {e}")

        # Set up line chart client
        self.line_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        self.line_client.on_connect = on_line_connect
        self.line_client.on_message = on_line_message
        
        # Set up subplot client
        self.subplot_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        self.subplot_client.on_connect = on_subplot_connect
        self.subplot_client.on_message = on_subplot_message
        
        try:
            self.line_client.connect(self.mqttBroker)
            self.line_client.loop_start()
            
            self.subplot_client.connect(self.mqttBroker)
            self.subplot_client.loop_start()
            
            print("MQTT clients connected and running")
        except Exception as e:
            print(f"Error connecting MQTT clients: {e}")
    
    def recieveForLineChart(self):
        # Just return the current data
        if self.line_chart_data is not None:
            return self.line_chart_data
        return None

    def recieveForSubPlot(self):
        # Just return the current data
        if self.subplot_data is not None:
            return self.subplot_data
        return None
        
    def disconnect(self):
        if self.line_client:
            self.line_client.loop_stop()
        if self.subplot_client:
            self.subplot_client.loop_stop()