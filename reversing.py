import streamlit as st

def reversing():
  st.write("""
  ## 3. Reversing a string
  If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.
  """)

  st.write("""
  ### Example
  """)

  code = '''
  str=”hello world!”
  a=str[::-1]
  print(a)
  '''
  st.code(code, language='python')
  st.download_button('Download Code', code)
  
  st.write("""
  ### Output
  """)

  code = '''
  !dlrow olleh
  '''
  st.code(code, language='python')
