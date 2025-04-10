from dao.TrackObjects import TrackObjects
from entity.Normalize import Normalize
from entity.StorePoints import StorePoints
from entity.Animal import Animal
from datetime import datetime
import time

class TrackObjectsImpl(TrackObjects):
    def __init__(self):
        self.all_points = StorePoints()

    def forLoopResults(self, resultTracker, curCls):
        all_x_points = []
        all_y_points = []
        escaped_animal = []
        trackedObjects = []
        shortestObjId = None
        minDist = float('inf')
        closestCoords = None
        id, dist = None, None
        x1, y1, x2, y2, w, h, cx, cy, new_x_, new_y_ = None, None, None, None, None, None, None, None, None, None

        for i in resultTracker:
            x1, y1, x2, y2, id = i
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cx, cy = x1 + w // 2, y1 + h // 2 
            new_x_, new_y_ = Normalize.map_coordinates(x=cx, y=cy, cameraOption=self.all_points.getcameraOption(), originalWidth=self.all_points.getoriginalWidth(), originalHeight=self.all_points.getoriginalHeight())
            all_x_points.append(self.all_points.getoriginalWidth() - cx)
            all_y_points.append(self.all_points.getoriginalHeight() - cy)

            escaped_id = [i[0] for i in self.all_points.getescapedAnimal()]
            if self.all_points.getboundaryLine()[1] - 20 < cy < self.all_points.getboundaryLine()[1] + 20 and id not in escaped_id:
                escaped_animal.append([int(id), curCls])
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                warningMsg = f"{curCls} is likely to escaped the marked boundary. {now} +5:30 UTC"

            dist = self.all_points.getoriginalHeight() - cy

            if dist < minDist:
                minDist = dist
                shortestObjId = id
                closestCoords = (cx, cy)
            
            objData = (x1, y1, x2, y2, w, h, cx, cy, id, dist)
            trackedObjects.append(objData)
            
        return x1, y1, x2, y2, w, h, cx, cy, new_x_, new_y_, escaped_animal, shortestObjId, closestCoords, minDist, id, dist, trackedObjects