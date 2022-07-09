import streamlit as st
from PIL import Image

style = open( "./pages/html/style.html")
st.markdown( style.read(), unsafe_allow_html=True )

st.sidebar.image( "./images/home.png", use_column_width=True)
st.sidebar.write('<style>body { margin: 0; font-family: Arial, Helvetica, sans-serif;} .header{padding: 10px 16px; background: #555; color: #f1f1f1; position:fixed;top:0;} .sticky { position: fixed; top: 0; width: 100%;} </style><div class="header" id="myHeader">FOIA Document Analysis</div>', unsafe_allow_html=True)

title_alignment="""
<style>
#team-ufo {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

colT1,colT2,colT3 = st.columns(3)
with colT2:
  st.title("Team UFO")
  st.markdown( "<p style=\"text-align: center;\">FOIA Document Analysis</p>", unsafe_allow_html=True)
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
