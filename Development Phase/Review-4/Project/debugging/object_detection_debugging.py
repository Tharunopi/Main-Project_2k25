from ultralytics import YOLO
import cv2, math, cvzone

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

model = YOLO('../../YOLO_weights/yolo11n.pt')

cap = cv2.VideoCapture(0)

cap.set(3, 1280) #width
cap.set(4, 720) #height

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    for i in results:
        boxes = i.boxes
        print(boxes)
        for j in boxes:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2- x1, y2-y1
            print(x1, y1, x2, y2)

            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil((j.conf[0] * 100)) / 100
            # cls = classNames[int(j.cls[0])]
            cls = j.cls[0]

            cvzone.putTextRect(img, f"cls:{cls} conf:{conf}", (max(0, x1), max(30, y1-10)))
            print(cls)

    cv2.imshow("webcam", img)
    cv2.waitKey(0)