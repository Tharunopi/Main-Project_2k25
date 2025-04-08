import serial

class ProcessESPData:
    def __init__(self, esp):
         self.esp = esp

    def process_esp_data(esp):
            current_distance = None

            if esp and esp.in_waiting > 0:
                try:
                    line = esp.readline().decode('utf-8', errors='replace').strip()
                    if line.startswith("DIST:"):
                        try:
                            distance = float(line[5:])
                            current_distance = distance
                        except ValueError:
                            pass
                except Exception as e:
                    print(f"Error reading from ESP8266: {e}")
                    esp.flushInput()
                    
            return current_distance