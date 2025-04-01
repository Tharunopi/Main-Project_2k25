import cv2
import math
import numpy as np
from ultralytics import YOLO
from sort import *
import streamlit as st
import matplotlib.pyplot as plt
import time

# Set page configuration
st.set_page_config(page_title="Hand Position Tracker", layout="wide")
st.title("Real-time Hand Position Map")

# Initialize model
@st.cache_resource
def load_model():
    return YOLO('../../YOLO_weights/best_hand_n.pt')

model = load_model()
classNames = ["Elephant"]  # Your class name - make sure this matches your model's class
ori_width, ori_height = 1280, 720

# Initialize tracker
tracker = Sort(max_age=40, min_hits=3, iou_threshold=0.3)

# Create the graph container
st.subheader("Hand Position Map")
position_plot = st.empty()

# Add a stop button
stop_button = st.button("Stop Tracking")

# Setup camera
cap = cv2.VideoCapture(0)
cap.set(3, ori_width)
cap.set(4, ori_height)

# Main loop
while cap.isOpened() and not stop_button:
    success, img = cap.read()
    if not success:
        st.error("Failed to capture image from camera")
        break

    # Process image with YOLO
    results = model(img, stream=True)
    dets = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cx, cy = x1 + w // 2, y1 + h // 2

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = classNames[int(box.cls[0])]

            # Make sure this matches the label in your YOLO model
            if conf >= 0.6:  # Confidence threshold
                cur_arr = np.array([x1, y1, x2, y2, conf])
                dets = np.vstack((dets, cur_arr))

    # Update tracker
    result_tracker = tracker.update(dets)

    # Extract positions and IDs
    x_positions = []
    y_positions = []
    ids = []

    for i in result_tracker:
        x1, y1, x2, y2, id = i
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        cx, cy = x1 + w // 2, y1 + h // 2

        x_positions.append(cx)
        y_positions.append(cy)
        ids.append(int(id))

    # Create and update the figure using plt instead of Figure directly
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, ori_width)
    ax.set_ylim(0, ori_height)
    ax.set_xlabel('X Position')
    ax.set_ylabel('Y Position')
    ax.set_title('Hand Position Map')
    ax.invert_yaxis()  # Invert y-axis to match camera coordinates

    # Add border lines around the plot area
    ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    ax.axhline(y=ori_height, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
    ax.axvline(x=ori_width, color='k', linestyle='-', alpha=0.3)

    if x_positions:
        # Plot the points with different colors based on ID
        scatter = ax.scatter(x_positions, y_positions, s=200, c=ids, cmap='rainbow')

        # Add ID labels
        for i, txt in enumerate(ids):
            ax.annotate(f"ID:{txt} ({x_positions[i]},{y_positions[i]})",
                        (x_positions[i], y_positions[i]),
                        xytext=(10, 10), textcoords="offset points",
                        fontsize=12, color='blue')

    # Add grid for better position reference
    ax.grid(True, alpha=0.5)

    # Update the plot in Streamlit
    position_plot.pyplot(fig)
    plt.close(fig)  # Important: close the figure to prevent memory leaks

    # Small delay to reduce CPU usage
    time.sleep(0.05)

# Release resources when stopped
cap.release()
st.write("Tracking stopped")