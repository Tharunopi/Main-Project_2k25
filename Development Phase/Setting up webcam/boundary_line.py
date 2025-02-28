import cv2

cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

while True:
   success, img = cap.read()
   cv2.line(img, (0, 650), (1280, 650), (255, 0, 255), 2)
   cv2.imshow("Image", img)
   cv2.waitKey(1)
