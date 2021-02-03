#Sequencing-----
mile = int(input("Please Enter your miles: "))# this allowes the user to input an integer which will be stored  
KM = mile * 1.6# this takes the stored integer and does a calculation 
print("Your distance is: ", KM, "in KM")# this prints the new integer 
if mile >= 100:# if the new integer is 100 or above it prints the line below
  print("I think you can stop now")
else:# if the new integer is below 100 it prints the line below 
  print("You can drive further")
