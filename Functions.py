def functionOne(localvariable):
  localvariable="hello"
  print (localvariable)

def functionTwo(parameter):
  print (parameter)

def functionThree(globalNumericvalue):
  global globalNumericvalue
  globalNumericvalue = globalNumericvalue + 2
  print(globalNumericvalue)