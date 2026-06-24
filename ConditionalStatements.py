

#Indentation : it means giving spaces at the begining of a line 
age=18
if age >=18:
    print("You can vote")

#If statement : it checks a condition,if the condition is true the code runs else nothing happens
temperature=25
if temperature>30:
    print("It 's a hot day")

#Assignment
marks=45
if marks>=40:
    print("You passed with:",marks)

#If,else statements: if condition is true then it will run the if block otherwise it will run the else block

age1=16
if age1>=18:
    print("You can vote")
else:
    print("You can't vote")

#Assignement

marks1=35
if marks1>=40:
    print("You passed with the total of",marks1)
else:
    print("You did not pass with the total of",marks1)

#Assignement1: write a program that checks the number is positive
num=int(input("Enter a random number:"))
if num>0:
    print("The number is positive")
else:
    print("The number is negative")

#Assignement2:write a program that checks whether a number is an odd or even number
number=int(input("Enter a number:"))
if number%2==0:
    print("The number is even")
else:
    print("The number is odd")
#Assignement:Take the user input and find out which one is larger
num2=int(input("Enter the 1st number:"))
num3=int(input("Enter the 2nd number:"))
if num2>num3:
    print(num2,"is greater than", num3)
else:
    print(num3,"is grater than",num2)

