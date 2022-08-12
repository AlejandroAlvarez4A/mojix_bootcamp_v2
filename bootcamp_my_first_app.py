import streamlit as st
import walrus 
import splitting
import reversing
import mergingTwoDictionaries
import zipFunction

from PIL import Image
image = Image.open('images/python.gif')
st.image(image, caption='Sunrise by the mountains')

text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

walrus.walrus()
splitting.splitting()
reversing.reversing()
mergingTwoDictionaries.merging()
zipFunction.zip()

