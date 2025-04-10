class ProcessESPData:
    def __init__(self, esp):
         self.esp = esp

    def process_esp_data(self):
            current_distance = None

            if self.esp and self.esp.in_waiting > 0:
                try:
                    line = self.esp.readline().decode('utf-8', errors='replace').strip()
                    if line.startswith("DIST:"):
                        try:
                            distance = float(line[5:])
                            current_distance = distance
                        except ValueError:
                            pass
                except Exception as e:
                    print(f"Error reading from ESP8266: {e}")
                    self.esp.flushInput()
                    
            return current_distance