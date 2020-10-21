#Sequencing-----
mile = int(input("Please Enter your miles: "))
KM = mile * 1.6
print("Your distance is: ", KM, "in KM")
if mile >= 100:
  print("I think you can stop now")
else:
  print("You can drive further")