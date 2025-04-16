import paho.mqtt.client as mqtt
import pickle, sys

sys.path.append(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4")

from dao.SendViaMQTT import SendViaMQTT

class SendViaMQTTImpl(SendViaMQTT):
    def __init__(self):
        mqttBroker = "mqtt.eclipseprojects.io"

        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION1)
        self.client.client_id = "Remote_Graph" 
        self.client.connect(mqttBroker)
        self.client.loop_start()

    def sendForLineChart(self):
        try:
            from dao.ChartsImpl import ChartsImpl
            charts = ChartsImpl()
            pickledDataFrame = pickle.dumps(charts.getForLineChart())
            self.client.publish("CXCYForLineChartTharun", pickledDataFrame)
            return True
        except:
            return False

    def sendForSubplot(self):
        try:
            from dao.ChartsImpl import ChartsImpl
            charts = ChartsImpl()
            pickledFig = pickle.dumps(charts.getForSubPlots())
            self.client.publish("CXCYForSubPlotTharun", pickledFig)
            return True
        except:
            return False