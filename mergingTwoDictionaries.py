import streamlit as st

def merging():
  st.write("""
  ## 4. Merging two dictionaries  
  This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:
  """)

  st.write("""
  ### Example
  """)

  code = '''
  d1 = {“a”: 10, “b”:20}
  d2 = {“c”: 30, “d”:40}
  d3 = {**d1, **d2}
  print(d3)
  '''
  st.code(code, language='python')
  st.download_button('Download Code', code)
  st.write("""
  ### Output
  """)

  code = '''
  {‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}
  '''
  st.code(code, language='python')
