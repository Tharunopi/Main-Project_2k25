# from ultralytics import YOLO
# import math, cvzone, cv2
#
# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"
#               ]
#
# model = YOLO("../../YOLO_weights/yolo11n.pt")
#
# cap = cv2.VideoCapture(0)
#
# cap.set(3, 1280) #width
# cap.set(4, 720) #height
#
# while True:
#     success, img = cap.read()
#
#     result = model(img, stream=True)
#
#     for i in result:
#         boxes = i.boxes
#         for j in boxes:
#             x1, y1, x2, y2 = j.xyxy[0]
#             conf = math.ceil((j.conf[0] * 100)) / 100
#             cls = classNames[int(j.cls[0])]
#
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             w, h = x2-x1, y2-y1
#             cx, cy = x1+w//2, y1+h//2
#
#             if cls in ["cell phone"] and conf >= 0.6:
#                 cvzone.cornerRect(img, (x1, y1, w, h))
#                 cvzone.putTextRect(img, f"cls:{cls} conf:{conf}", (max(0, x1), max(30, y1-10)))
#                 cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
#
#                 print(x1, y1, x2, y2)
#
#     cv2.imshow("webcam", img)
#     cv2.waitKey(1)

# import serial
# import time
# import cv2
# from ultralytics import YOLO
# import math
# import cvzone
#
# # Initialize Serial Communication
# arduino = serial.Serial('COM24', 9600)  # Change to your Arduino port
# time.sleep(2)  # Allow time for connection
#
# # YOLO Model
# model = YOLO("../../YOLO_weights/yolo11s.pt")
#
# # Video Capture
# cap = cv2.VideoCapture(0)
# cap.set(3, 1280)  # width
# cap.set(4, 720)  # height
#
# # Servo Angles
# servoX, servoY = 0, 0  # Default center position
#
# # Frame Center
# frameCenterX, frameCenterY = 1280 // 2, 720 // 2
#
# # Last detection time
# last_detection_time = time.time()
# DETECTION_TIMEOUT = 5  # Seconds before resetting to 90°
#
# while True:
#     success, img = cap.read()
#     if not success:
#         continue
#
#     result = model(img, stream=True)
#     object_detected = False
#
#     for i in result:
#         boxes = i.boxes
#         for j in boxes:
#             x1, y1, x2, y2 = j.xyxy[0]
#             conf = math.ceil((j.conf[0] * 100)) / 100
#             cls = "cell phone" if int(j.cls[0]) == 67 else ""
#
#             if cls == "cell phone" and conf >= 0.6:
#                 object_detected = True  # Mark detection
#                 x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#                 w, h = x2 - x1, y2 - y1
#                 cx, cy = x1 + w // 2, y1 + h // 2  # Object center
#
#
#                 # Move Servo Based on Detected Position
#                 errorX = frameCenterX - cx  # Left (-), Right (+)
#                 errorY = frameCenterY - cy  # Up (-), Down (+)
#
#                 # Adjust angles based on error
#                 if abs(errorX) > 5:  # Tolerance
#                     servoX += 5 if errorX > 0 else -5  # Right/Left movement
#                 if abs(errorY) > 5:  # Tolerance
#                     servoY += 5 if errorY < 0 else -5  # FIXED: Inverted the Y movement
#
#                 # Clamp angles
#                 servoX = max(0, min(180, servoX))
#                 servoY = max(0, min(180, servoY))
#
#                 print(f"Error X: {errorX}, Error Y: {errorY}")
#                 print(f"Servo X: {servoX}, Servo Y: {servoY}")
#
#                 # Send to Arduino
#                 arduino.write(f"{servoX},{servoY}\n".encode())
#
#                 # Draw Detection
#                 cvzone.cornerRect(img, (x1, y1, w, h))
#                 cvzone.putTextRect(img, f"cls:{cls} conf:{conf}", (max(0, x1), max(30, y1 - 10)))
#                 cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
#
#     # If no object detected for a while, reset to 90°
#     if not object_detected and (time.time() - last_detection_time) > DETECTION_TIMEOUT:
#         servoX, servoY = 90, 90  # Reset position
#         arduino.write(f"{servoX},{servoY}\n".encode())
#         last_detection_time = time.time()  # Update last reset time
#     elif object_detected:
#         last_detection_time = time.time()  # Reset timer if object detected
#
#     cv2.imshow("webcam", img)
#     cv2.waitKey(1)

import serial
import time
import cv2
from ultralytics import YOLO
import math
import cvzone

# Initialize Serial Communication
arduino = serial.Serial('COM24', 9600)  # Change to your Arduino port
time.sleep(2)  # Allow time for connection

# YOLO Model
model = YOLO("../../YOLO_weights/yolo11s.pt")

# Video Capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height

# Control Parameters
Kp = 0.3  # Proportional gain - adjust this value to change sensitivity
center_position = 90
servoX = center_position
servoY = center_position

# Frame Center
frameCenterX = 1280 // 2
frameCenterY = 720 // 2

# Last detection time
last_detection_time = time.time()
DETECTION_TIMEOUT = 2  # Seconds before resetting to center

while True:
    success, img = cap.read()
    if not success:
        continue

    result = model(img, stream=True)
    object_detected = False

    for i in result:
        boxes = i.boxes
        for j in boxes:
            x1, y1, x2, y2 = j.xyxy[0]
            conf = math.ceil((j.conf[0] * 100)) / 100
            cls = "cell phone" if int(j.cls[0]) == 67 else ""

            if cls == "cell phone" and conf >= 0.1:
                object_detected = True
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                cx, cy = x1 + w // 2, y1 + h // 2

                # Calculate errors
                errorX = frameCenterX - cx
                errorY = frameCenterY - cy

                # Calculate new servo positions using proportional control
                servoX = center_position + (errorX * Kp)
                servoY = center_position + (errorY * Kp)

                # Clamp angles to valid range
                servoX = max(0, min(180, servoX))
                servoY = max(0, min(180, servoY))

                # Send to Arduino
                command = f"{int(servoX)},{int(servoY)}\n"
                arduino.write(command.encode())

                # Debug print
                print(f"Error X: {errorX}, Error Y: {errorY}")
                print(f"Servo X: {int(servoX)}, Servo Y: {int(servoY)}")

                # Draw Detection
                cvzone.cornerRect(img, (x1, y1, w, h))
                cvzone.putTextRect(img, f"Phone: {conf:.2f}", (max(0, x1), max(30, y1 - 10)))
                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                # Draw center lines
                cv2.line(img, (frameCenterX, 0), (frameCenterX, 720), (0, 255, 0), 1)
                cv2.line(img, (0, frameCenterY), (1280, frameCenterY), (0, 255, 0), 1)

    # Reset to center if no detection
    if not object_detected and (time.time() - last_detection_time) > DETECTION_TIMEOUT:
        servoX = center_position
        servoY = center_position
        arduino.write(f"{center_position},{center_position}\n".encode())
        last_detection_time = time.time()
    elif object_detected:
        last_detection_time = time.time()

    cv2.imshow("Object Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()