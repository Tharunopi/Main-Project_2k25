from ultralytics import YOLO
import cv2, math, cvzone, time, serial

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
ori_width, ori_height = 640, 480
target_width, target_height = 180, 180
esp = serial.Serial("COM24", 9600, )
time.sleep(2)

def map_coordinates(x, y):
    new_x = target_width - int((x * target_width) / ori_width)

    new_y = int((y * target_height) / ori_height)

    return new_x, new_y

model = YOLO('../../YOLO_weights/yolo11n.pt')

cap = cv2.VideoCapture(0)

cap.set(3, ori_width) #width
cap.set(4, ori_height) #height

last_detection_time = time.time()
default_position_sent = False

while True:
    success, img = cap.read()
    if success:
        results = model(img, stream=True)
        object_detected = False

        for i in results:
            boxes = i.boxes
            for j in boxes:
                x1, y1, x2, y2 = j.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2- x1, y2-y1
                cx, cy = x1 + w // 2, y1 + h // 2

                conf = math.ceil((j.conf[0] * 100)) / 100
                cls = classNames[int(j.cls[0])]

                if cls in ["cell phone"] and conf >= 0.1:
                    object_detected = True
                    last_detection_time = time.time()
                    default_position_sent = False

                    new_x, new_y = map_coordinates(cx, cy)
                    data = f"{new_x},{new_y}\n"
                    esp.write(data.encode())
                    print(f"center: {cx} -- altered: {new_x}")
                    print(f"center: {cy} -- altered: {new_y}")

                    cvzone.cornerRect(img, (x1, y1, w, h))
                    cvzone.putTextRect(img, f"cls:{cls} conf:{conf}", (max(0, x1), max(30, y1-10)))
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

        # Check if 3 seconds passed without detection
        if not object_detected and time.time() - last_detection_time > 3 and not default_position_sent:
            default_position_sent = True
            data = "90,90\n"
            esp.write(data.encode())
            print("No object detected for 3 seconds, setting to default position")

    cv2.imshow("webcam", img)
    cv2.waitKey(1)