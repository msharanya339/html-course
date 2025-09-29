def add(a,b):
    return a + b

def subtraction(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtraction(num1, num2)}")
print(f"{num1} * {num2} = {multiply(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")