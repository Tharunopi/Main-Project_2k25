import streamlit as st
import cv2

st.title("WebCam")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("Calibration", img)
    cv2.waitKey(1)