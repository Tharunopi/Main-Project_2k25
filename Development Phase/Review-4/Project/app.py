import streamlit as st
import cv2, time
import pandas as pd

from entity.ProcessAllAnimal import ProcessAllAnimal
from forStreamLit import getFrameForStreamlit

st.title("AI-Driven Fencing")

imgHolder = st.empty()
cameraHolder = st.sidebar.title("Camera: 1")
locationHolder = st.sidebar.title("South Zone TamilNadu")

escapeCountHolder = st.sidebar.empty()
escapedAnimalHolder = st.sidebar.empty()

xMovements, yMovements = st.sidebar.columns(2)


fullAnimalDetails = st.sidebar.empty()
warningMessagePlaceHolder = st.empty()

old_x, old_y = 90, 90

while True:
    img, escapeCount, escapedAnimal, newEscapes, allAnimal, new_x, new_y = getFrameForStreamlit()

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    escapeCountHolder.text(f"Escaped: {escapeCount}")

    if escapedAnimal is not None:
        escapedAnimalHolder.text(f"Escaped Animal Category: {', '.join(str(i) for i in escapedAnimal)}")

    if allAnimal:
        newAllAnimals = ProcessAllAnimal.processallAnimal(allAnimal=allAnimal)
        dfAllAnimal = pd.DataFrame(newAllAnimals)
        fullAnimalDetails.table(dfAllAnimal)

    if newEscapes:
        for i in newEscapes:
            with warningMessagePlaceHolder:
                st.warning(f"{i[1]} is likely to escaped the marked boundary. {i[2]} +5:30 UTC")

        newEscapes = None

    if new_x and new_y:
        diffX = new_x - old_x
        diffY = new_y - old_y

        with xMovements:
            st.metric("X-Movement", f"{new_x}", f"{diffX}", border=True)
        with yMovements:
            st.metric("Y-Movement", f"{new_y}", f"{diffY}", border=True)

        old_x = new_x
        old_y = new_y

    imgHolder.image(img_rgb, channels="RGB")
