import cv2

cap = cv2.VideoCapture(2)

while True:
    success, img = cap.read()

    cv2.imshow("mobile cam", img)