#< > greater or less then
#==  is it equal to
# >= greater than or equal to
# != NOT Equal to
 
myNumber = 15
otherNumber = int(input("Please enter a number: "))
 
if myNumber < otherNumber:
    print("Your number is bigger than mine")
 
elif otherNumber < myNumber:
      print("My number is bigger than yours")
else :
     print("You chose the same number as me")
 
# FizzBuzz
#Get a number from the User and print:
#"Fizz" if the number is divisible by 3
# "Buzz" if the number is divisible by 5
#and if neither print the number
number = int(input("Enter a number:"))
# the % operator divides the number and checks the remainder
#eg 7 % 3 would equal 2 with a remainder of 1
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 5 == 0:
    print("Buzz")
elif   number % 3 == 0:
    print("Fizz")
else:
    print(number)
 