import streamlit as st

st.write("Hello from the mojix bootcamp")

st.write("""
# 1. Walrus operator
The Walrus or **:=** `operator` is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
""")

code = '''def hello():
     print("Hello, Streamlit!")'''

st.code(code, language='python')