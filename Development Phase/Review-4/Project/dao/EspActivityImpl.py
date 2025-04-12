import time

from dao.EspActivity import EspActivity
from entity.Normalize import Normalize
from entity.ProcessESPData import ProcessESPData

from util.ESP8266Connection import ESP8266Connection

class EspActivityImpl(EspActivity):
    def __init__(self):
        self.defaultPositionSent = False
        self.esp = ESP8266Connection.getConnection()

    def espManipulation(self, shortestObjId, closestCoords):
        try:
            espData = ProcessESPData(esp=self.esp)
            distance = espData.process_esp_data()

            currentDistance = None

            if distance is not None:
                currentDistance = distance
                

            if shortestObjId is not None and closestCoords is not None:
                cx, cy = closestCoords
                new_x, new_y = Normalize.map_coordinates(cx, cy)
                if self.esp:
                    data = f"{new_x},{new_y}\n"
                    self.esp.write(data.encode())
                    self.defaultPositionSent = False

                return (new_x, new_y, currentDistance)

        except Exception as e:
            print(f"Error: {e}")

    def skipTime(self, lastDetectionTime):
        timeDiff = time.time() - lastDetectionTime

        if timeDiff > 3 and self.defaultPositionSent == False and self.esp is not None:
                data = "90,90\n"
                self.esp.write(data.encode())
                self.defaultPositionSent = True
                with open("log.txt", 'w') as f:
                    f.write(f"{self.defaultPositionSent}, {timeDiff}")
                return True