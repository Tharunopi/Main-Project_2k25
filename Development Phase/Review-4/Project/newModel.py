from ultralytics import YOLO
import cv2, math, cvzone

cap = cv2.VideoCapture(r"C:\Stack overflow\Main-Project_2k25\YOLO_weights\ALL Animals\just-don-t-move-720-ytshorts.savetube.me.mp4")

model = YOLO(r"C:\Stack overflow\Main-Project_2k25\Development Phase\Review-4\YOLO_weights\best_final.pt")
classNames = ['bear', 'boar', 'elephant', 'leopard', 'tiger']

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for i in results:
        boxes = i.boxes
        for j in boxes:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cx, cy = x1 + w // 2, y1 + h // 2

            conf = math.ceil((j.conf[0] * 100)) / 100
            cls = classNames[int(j.cls[0])]

            if conf >= 0.6:
                cvzone.putTextRect(img, f"conf:{conf}", (max(0, x1), max(30, y2 + 40)), offset=2)
                cvzone.cornerRect(img, (x1, y1, w, h), )

    cv2.imshow("new", img)
    cv2.waitKey(1)