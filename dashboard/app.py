import os
import streamlit as st
import numpy as np
from PIL import  Image


# Custom imports 
from multipage import MultiPage
from pages import home,load,loan,info # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('logo.png')
display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
col1, col2 = st.columns(2)
col1.image(display, width = 400)

# Add all your application here
app.add_page("Home", home.app)
app.add_page("Chargement", load.app)
app.add_page("Demande de prêt", loan.app)
app.add_page("Information", info.app)



# The main app
app.run()
