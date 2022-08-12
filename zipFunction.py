import streamlit as st

def zip():
  st.write("""
  ## 5. The zip() function
  The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.
  """)

  st.write("""
  ### Example
  """)

  code = '''
  colour = [“red”, “yellow”, “green”]
  fruits = [‘apple’, ‘banana’, ‘mango’]
  for colour, fruits in zip(colour, fruits):
  print(colour, fruits)
  '''
  st.code(code, language='python')

  st.write("""
  ### Output
  """)

  code = '''
  red apple
  yellow banana
  green mango
  '''
  st.code(code, language='python')

  st.write("""
  The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.
  """)
  
  st.write("""
  ### Example
  """)

  code = '''
  students = [“Rajesh”, “kumar”, “Kriti”]
  marks = [87, 90, 88]
  dictionary = dict(zip(students, marks))
  print(dictionary)
  '''
  st.code(code, language='python')

  st.write("""
  ### Output
  """)

  code = '''
  {‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}
  '''
  st.code(code, language='python')