from ultralytics import YOLO
import cv2, math, cvzone, time, serial
from sort import *
import numpy as np

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

ori_width, ori_height = 1280, 720
target_width, target_height = 180, 180

# Setup ESP8266 connection
try:
    esp = serial.Serial("COM24", 9600, timeout=1)  # Update with your COM port
    time.sleep(2)
    esp.flushInput()
    print("ESP8266 connected successfully")
except Exception as e:
    print(f"Error connecting to ESP8266: {e}")
    esp = None


def map_coordinates(x, y):
    new_x = target_width - int((x * target_width) / ori_width)
    new_y = int((y * target_height) / ori_height)
    return new_x, new_y


# Process incoming data from ESP8266
def process_esp_data():
    current_distance = None
    if esp and esp.in_waiting > 0:
        try:
            line = esp.readline().decode('utf-8', errors='replace').strip()
            if line.startswith("DIST:"):
                try:
                    distance = float(line[5:])  # Remove "DIST:" prefix
                    current_distance = distance
                except ValueError:
                    pass
        except Exception as e:
            print(f"Error reading from ESP8266: {e}")
            esp.flushInput()
    return current_distance


model = YOLO('../../YOLO_weights/yolo11n.pt')
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

cap = cv2.VideoCapture(0)
cap.set(3, ori_width)
cap.set(4, ori_height)

last_detection_time = time.time()
default_position_sent = False
current_distance = None

while True:
    # Process any incoming data from ESP8266
    distance = process_esp_data()
    if distance is not None:
        current_distance = distance

    success, img = cap.read()
    results = model(img, stream=True)
    dets = np.empty((0, 5))
    object_detected = False

    for i in results:
        boxes = i.boxes
        for j in boxes:
            x1, y1, x2, y2 = j.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cx, cy = x1 + w // 2, y1 + h // 2

            conf = math.ceil((j.conf[0] * 100)) / 100
            cls = classNames[int(j.cls[0])]

            if cls in ["cell phone"] and conf >= 0.1:
                cur_arr = np.array([x1, y1, x2, y2, conf])
                dets = np.vstack((dets, cur_arr))
                object_detected = True
                last_detection_time = time.time()
                cvzone.putTextRect(img, f"conf:{conf}", (max(0, x1), max(30, y2 + 40)))

    result_tracker = tracker.update(dets)
    shortest_obj_id = None
    min_dist = float('inf')
    closest_coords = None

    for i in result_tracker:
        x1, y1, x2, y2, id = i
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2

        dist = ori_height - cy

        if dist < min_dist:
            min_dist = dist
            shortest_obj_id = id
            closest_coords = (cx, cy)

        cvzone.cornerRect(img, (x1, y1, w, h))
        cvzone.putTextRect(img, f"id:{id}, dist:{dist}", (max(0, x1), max(30, y1 - 10)))
        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (cx, cy), (cx, ori_height), (0, 255, 0), 1)

    # Check if we have a valid object to track
    if shortest_obj_id is not None and closest_coords is not None:
        cx, cy = closest_coords
        new_x, new_y = map_coordinates(cx, cy)

        # Send coordinates to servo controller
        if esp:
            data = f"{new_x},{new_y}\n"
            esp.write(data.encode())

        print(f"center: {cx} -- altered: {new_x}")
        print(f"center: {cy} -- altered: {new_y}")

        # Display distance if available
        if current_distance is not None:
            cvzone.putTextRect(img, f"id:{shortest_obj_id}, dist:{min_dist}, distance:{current_distance}cm", (max(0, 0), max(30, 0)))
            default_position_sent = False
        else:
            cvzone.putTextRect(img, f"id:{shortest_obj_id}, dist:{min_dist}",
                               (max(0, 0), max(30, 0)))
            default_position_sent = False

    # If no object detected for 3 seconds, reset to default position
    elif time.time() - last_detection_time > 3 and not default_position_sent and esp:
        data = "90,90\n"
        esp.write(data.encode())
        default_position_sent = True

    else:
        cvzone.putTextRect(img, f"No Objects Detected to track",
                           (max(0, 0), max(30, 0)))

    # Draw reference lines
    cv2.line(img, (ori_width // 2, 0), (ori_width // 2, ori_height), (255, 0, 255), 1)
    cv2.line(img, (0, ori_height // 2), (ori_width, ori_height // 2), (255, 0, 255), 1)

    # Show the image with all annotations
    cv2.imshow("webcam", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Press Esc to exit
        break

if esp:
    esp.close()
cap.release()
cv2.destroyAllWindows()