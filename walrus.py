def walrus():
  st.write("""
  ## 1. Walrus operator
  The Walrus or **:=** operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.
  """)

  st.write("""
  ### Example
  If we want to check and print the length of a list:
  """)

  code = '''
  Mylist = [1,2,3]
  if(l := len(mylist) > 2)
  print(l)
  '''
  st.code(code, language='python')

  st.write("""
  ### Output
  If we want to check and print the length of a list:
  """)

  code = '''
  3
  '''
  st.code(code, language='python')
