import streamlit as st
from PIL import Image

st.sidebar.image( "./images/home.png", use_column_width=True)

colT1,colT2,colT3 = st.columns(3)
with colT2:
  st.title("Team UFO")
with colT1:
  ufoImg = Image.open('./images/favpng_roswell-unidentified-flying-object-sprite.png')
  st.image(ufoImg, width=200)
with colT3:
  tsImg = Image.open('./images/favpng_united-states-youtube-clip-art.png')
  st.image( tsImg, width=275 )

intro = open( "./content/intro.md")

sections = open( "./content/sections.md")

st.markdown( intro.read() )

st.markdown( sections.read() )
