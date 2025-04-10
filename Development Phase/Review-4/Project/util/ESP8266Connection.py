import serial, time

class ESP8266Connection:
    @staticmethod
    def getConnection():
        esp = None
        try:
            esp = serial.Serial("COM24", 9600, timeout=1)
            time.sleep(2)
            esp.flushInput()
            return esp
        except Exception as e:
            print(f"Error connecting to ESP8266: {e}")
            return None