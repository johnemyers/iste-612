import streamlit as st
from PIL import Image


colT1,colT2,colT3 = st.columns(3)
with colT2:
  st.title("Team UFO")
with colT1:
  ufoImg = Image.open('./images/favpng_roswell-unidentified-flying-object-sprite.png')
  st.image(ufoImg, width=300)
with colT3:
  tsImg = Image.open('./images/favpng_united-states-youtube-clip-art.png')
  st.image( tsImg, width=300 )

