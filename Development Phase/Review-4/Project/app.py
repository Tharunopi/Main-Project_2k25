import streamlit as st
import cv2, time
from forStreamLit import getFrameForStreamlit

st.title("AI-Driven Fencing")

imgHolder = st.empty()
cameraHolder = st.sidebar.title("Camera: 1")
locationHolder = st.sidebar.title("South Zone TamilNadu")

escapeCountHolder = st.sidebar.empty()
escapedAnimalHolder = st.sidebar.empty()

while True:
    img, escapeCount, escapedAnimal = getFrameForStreamlit()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    escapeCountHolder.text(f"Escaped: {escapeCount}")

    if escapedAnimal is not None:
        escapedAnimalHolder.text(f"Escaped Animal Category: {', '.join(str(i) for i in escapedAnimal)}")

    imgHolder.image(img_rgb, channels="RGB")
