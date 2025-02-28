from ultralytics import YOLO
import cv2

model = YOLO('../YOLO_weights/yolo11n.pt')

results = model("D:/aqeel.jpg", show=True)

cv2.waitKey(0)