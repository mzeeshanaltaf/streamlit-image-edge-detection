import streamlit as st
import numpy as np
from PIL import Image
import cv2

page_title = "Image Edge Detection"
page_icon = "🖌️"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")

st.title(page_title)
st.write(":green[***Edge detection using Canny Edge detection technique***]")
st.write("This web app 🖥️ allows users to upload an image 🖼️ and detect its edges ✂️. Users can adjust the threshold "
         "value 🎚️ to fine-tune the edge detection process. It offers an interactive way to explore edge detection and "
         "visualize the results in real-time ⏱️")
st.subheader("Upload an Image")
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

if uploaded_image:
    st.subheader("Configuration")
    threshold = st.slider("Threshold", 0, 255, 0, 10)

    # Open the uploaded image, convert it to format readable by opencv, resize and change to gray scale
    image_o = np.array(Image.open(uploaded_image))
    img_resize = cv2.resize(image_o, (512, 512))
    img_gs = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)

    st.subheader("Result")
    col1, col2 = st.columns(2, vertical_alignment="bottom")
    with col1:
        st.image(img_resize)

    with col2:
        # st.write(':blue[***Edge Detection***]')
        edge_detection_img = cv2.Canny(img_gs, threshold, 255)
        st.image(edge_detection_img)

