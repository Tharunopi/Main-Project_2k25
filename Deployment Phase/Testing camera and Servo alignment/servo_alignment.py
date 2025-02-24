import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    h, w, _ = img.shape
    cv2.line(img, (w // 2, 0), (w // 2, h), (0, 255, 0), 2)
    cv2.line(img, (0, h // 2), (w, h // 2), (0, 255, 0), 2)

    cv2.imshow("Calibration", img)
    cv2.waitKey(1)

