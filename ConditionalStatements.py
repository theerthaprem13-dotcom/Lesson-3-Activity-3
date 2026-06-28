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

#If-elif-else statement: it is used when there are multiple conditions
marks2=81

if marks2>=90:
    print("Grade A+")
if marks2>=91:
    print("Grade A++")
elif marks2>=80:
    print("Grade A")
elif marks2>=81:
    print("Grade O")
else:
    print("Grade B")

#Logical operators: it combines multiple conditions(and,or,not)
#and operator: it works when both the conditions are true

#or operator: it works when atleast one condition must be true

#not operator: it reversees the result

#programme on and operator

permission_slip=False
fee_submitted= False

if permission_slip and fee_submitted:
    print("You can go to the trip")
else:
    print("You can't go to the trip")

#Programme on or operator
student=False
teacher=False

if student or teacher:
    print(" You can participate")
else:
    print(" You can't participate")

#Not operator
homework_completed=False

if not homework_completed:
    print("Please complete your homework",homework_completed)
else:
    print("Good Job!")

#Programme on school scholarship system

marks3=88
attendance=92

if marks3>=90 and attendance>=90:
    print("Full scholarship")
elif marks3>=80 or attendance>=95:
    print("Special consideration")
else:
    print("No scholarship")

#Assignement: write a programme where the user input is taken for student's age, if age is less than 13 and greater than 10 then print child else print a teen
age2=int(input("Enter your age:"))

if age2<13 and age2>10:
    print("You are a tween")
elif age2<10:
    print("You are a child")
else:
    print("You are a teen")



