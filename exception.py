try:
    num1,num2=eval(input("Enter two numbers,seperated by a comma:"))
    result=num1/num2
    print("The result is",result)
except ZeroDivisionError:
  print("Division by zero is error")

except SyntaxError:
   print("Comma is missing, enter number is seperated by a comma")

except:
    print("Wrong input")

finally:
   print("This will execute no matter what")