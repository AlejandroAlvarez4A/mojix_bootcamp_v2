import streamlit as st
import walrus 
import splitting
import reversing
import mergingTwoDictionaries
import zipFunction
from PIL import Image
image = Image.open('images/python.gif')

st.write("# 5 Cool Beginner Python Tricks That Will Make Your Life Easier")
st.image(image)
st.write("""
The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities.
In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.
""")

walrus.walrus()
splitting.splitting()
reversing.reversing()
mergingTwoDictionaries.merging()
zipFunction.zip()

st.write("# Conclusion")
st.write("""
These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website.

Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me.

However, the recommended resource is experienced by me and helped me in my data science career journey.
""")
