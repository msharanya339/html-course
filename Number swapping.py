
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

a, b, c = b, c, a

print(f"After swapping: a = {a}, b = {b}, c = {c}")