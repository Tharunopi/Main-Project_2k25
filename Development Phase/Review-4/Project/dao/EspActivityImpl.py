import time

from dao.EspActivity import EspActivity
from entity.Normalize import Normalize
from entity.ProcessESPData import ProcessESPData

from util.ESP8266Connection import ESP8266Connection

class EspActivityImpl(EspActivity):
    def espManipulation(self, shortestObjId, closestCoords, lastDetectionTime):
        esp = ESP8266Connection.getConnection()
        espData = ProcessESPData(esp=esp)
        distance = espData.process_esp_data()

        currentDistance = None

        if distance is not None:
            currentDistance = distance

        if shortestObjId is not None and closestCoords is not None:
            cx, cy = closestCoords
            new_x, new_y = Normalize.map_coordinates(cx, cy)
            if esp:
                data = f"{new_x},{new_y}\n"
                esp.write(data.encode())

            if currentDistance is not None:
                default_position_sent = False

            else:
                default_position_sent = False

        elif time.time() - lastDetectionTime > 3 and not default_position_sent and esp:
            data = "90,90\n"
            esp.write(data.encode())
            default_position_sent = True

        else:
            detectionStatus = "No objects Detected"