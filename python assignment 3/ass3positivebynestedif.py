# check the number is postive are not by using nested if
num = int(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print(" you entered a zero")
   else:
       print("you entered a positive number")
else:
   print("you entered a negative number")