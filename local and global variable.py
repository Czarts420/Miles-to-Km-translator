def myfunc():# this is a function storing a global variable 
  global x
  x = "a bad idea"# this is the global variable 

myfunc()# the global variable can be used out of the function 

print("Second lockdown is " + x)# this prints the global variable 

def SayHello():# this is a function storing a local variable 
    user='John'
    print ("user = ", SayHello)# this prints the local variable 
SayHello()# the local variable can only be used within the function
