import cv2, cvzone

from dao.DetectObjectsImpl import DetectObjectsImpl

from entity.Camera import Camera
from entity.StorePoints import StorePoints

from util.ModelLoading import ModelLoading

points = StorePoints()
modelLoad = ModelLoading()
detectObjects = DetectObjectsImpl()

model = modelLoad.loadModel()
cam = Camera(points.getoriginalWidth(), points.getoriginalHeight())

while True:
    img = cam.getFrame()

    results = model(img, stream=True)
    conf, cls, x1, y1, x2, y2, w, h, cx, cy = detectObjects.forLoopResults(results)
    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
    cv2.imshow("Camera", img)
    cv2.waitKey(1)