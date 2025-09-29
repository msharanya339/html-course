def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input("Enter a number:"))

if num < 0:
     print("Cannot get factorial for negative numbers!")
else:
     print(f"The factorial of{num} is {factorial(num)}")