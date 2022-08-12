import streamlit as st
import walrus 
import splitting
import reversing
import mergingTwoDictionaries
import zipFunction
from PIL import Image
image = Image.open('images/python.gif')

st.write("# 10 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.image(image, caption='Python')
st.write("""
The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.
In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.
""")
text_contents = '''Tutorial'''
st.download_button('Download Tutorial', text_contents)

walrus.walrus()
splitting.splitting()
reversing.reversing()
mergingTwoDictionaries.merging()
zipFunction.zip()

