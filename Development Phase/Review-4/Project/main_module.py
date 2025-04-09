import cv2, cvzone
import numpy as np

from dao.DetectObjectsImpl import DetectObjectsImpl
from dao.TrackObjectsImpl import TrackObjectsImpl

from entity.Camera import Camera
from entity.StorePoints import StorePoints

from util.ModelLoading import ModelLoading

points = StorePoints()
modelLoad = ModelLoading()
detectObjects = DetectObjectsImpl()
trackObjects = TrackObjectsImpl()

model = modelLoad.loadModel()
cam = Camera(points.getoriginalWidth(), points.getoriginalHeight())

while True:
    img = cam.getFrame()

    results = model(img, stream=True)
    dets = np.empty((0, 5))
    curCls = None

    conf, cls, x1, y1, x2, y2, w, h, cx, cy, dets = detectObjects.forLoopResults(results=results, dets=dets, curCls=curCls)

    resultTracker = 

    x1, y1, x2, y2, w, h, cx, cy, new_x_, new_y_, escaped_animal, shortestObjId, closestCoords = trackObjects.forLoopResults()

    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    cv2.imshow("Camera", img)
    cv2.waitKey(1)