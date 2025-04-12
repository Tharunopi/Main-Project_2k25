import cv2, cvzone, time, sys
import numpy as np

sys.path.append(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\Project")

from dao.DetectObjectsImpl import DetectObjectsImpl
from dao.TrackObjectsImpl import TrackObjectsImpl
from dao.EspActivityImpl import EspActivityImpl
from dao.ChartsImpl import ChartsImpl

from entity.Camera import Camera
from entity.StorePoints import StorePoints

from util.ModelLoading import ModelLoading
from util.TrackerLoading import TrackerLoading

modelLoad = ModelLoading()
detectObjects = DetectObjectsImpl()
trackObjects = TrackObjectsImpl()
points = trackObjects.all_points
espActivity = EspActivityImpl()

model = modelLoad.loadModel()
tracker = TrackerLoading.loadTracker()
cam = Camera(points.getoriginalWidth(), points.getoriginalHeight())
lastDetectionTime = time.time()

escapeCount = 0
escapedAnimal = None
newEscapes = None
allAnimal = None
new_x, new_y = 0, 0

def getFrameForStreamlit():
    global lastDetectionTime
    global escapeCount
    global escapedAnimal
    global newEscapes
    global allAnimal
    global new_x
    global new_y

    img = cam.getFrame()

    results = model(img, stream=True)
    dets = np.empty((0, 5))
    curCls = None

    conf, curCls, x1, y1, x2, y2, w, h, cx, cy, dets, lastDetectionTime = detectObjects.forLoopResults(results=results, dets=dets, curCls=curCls, lastDetectionTime=lastDetectionTime)

    resultTracker = tracker.update(dets=dets)
    if len(resultTracker) > 0:

        x1, y1, x2, y2, w, h, cx, cy, new_x_, new_y_, escapedAnimal, shortestObjId, closestCoords, minDist, id, dist, trackedObjects, newEscapes, allAnimal = trackObjects.forLoopResults(resultTracker=resultTracker, curCls=curCls)

        new_x, new_y, currentDistance = espActivity.espManipulation(shortestObjId=shortestObjId, closestCoords=closestCoords)
        points.updatedistanceHisory(currentDistance)
        points.updatepixelDistanceHistory(minDist)

        for i in trackedObjects:
            x1, y1, x2, y2, w, h, cx, cy, id, dist = i
            cvzone.cornerRect(img, (x1, y1, w, h), )
            cvzone.putTextRect(img, f"conf:{conf}, cls:{curCls}", (max(0, x1), max(30, y2 + 40)), offset=2)
            cvzone.putTextRect(img, f"id:{id}, dist:{dist}", (max(0, x1), max(30, y1 - 10)), offset=2)
            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        escapeCount = points.getEscapeCount()
        cvzone.putTextRect(img, f"Cam:1 Object Detected - Escaped: {escapeCount}", (max(0, 10), max(30, 10)), offset=2)
        
    
    else:
        status = espActivity.skipTime(lastDetectionTime=lastDetectionTime)
        cvzone.putTextRect(img, f"Cam:1 No Objects Detected", (max(0, 10), max(30, 10)), offset=2)

    return img, escapeCount, escapedAnimal, newEscapes, allAnimal, new_x, new_y