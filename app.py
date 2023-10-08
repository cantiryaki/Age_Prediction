# import libraries
import streamlit as st
import numpy as np
import cv2 
from PIL import Image
from face import extractFaces,classify_face
import imageio.v3 as iio

st.title(':smile: Age Estimation :smile:')
image = Image.open("./media/ages.png")
st.image(image, caption='Facial Ages Images', width=500)


uploaded_file = st.file_uploader("Choose a CSV file",  type= ['png', 'jpg'])
img=None
if uploaded_file is not None:
    img = iio.imread(uploaded_file)

    img = cv2.resize(img,dsize=(300,300), interpolation=cv2.INTER_CUBIC)
    st.image(img, caption='Uploaded Image Images')

predict = st.button("Predict")
#stop = st.button("stop camera")

FRAME_WINDOW = st.image([])


if predict and img is not None:

        face, bbox = extractFaces(img)

            # no face or multiple faces
        if type(face)==str:
            frame = cv2.putText(img, face, (70,100), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (0, 0, 255), 2, cv2.LINE_AA)
        else:
                frame = cv2.rectangle(img, (bbox[0],bbox[1]), (bbox[2]+bbox[0],bbox[1]+bbox[3]), (0,255,0), 2)

              
                result = classify_face(face)       
   
                frame = cv2.putText(frame, f"Age: {str(result)}", (70,100), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2, cv2.LINE_AA)    
        
        FRAME_WINDOW.image(frame)


      