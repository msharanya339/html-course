Marks = float(input("Enter your marks out of 100: "))
total = 100

bmi = Marks/total*100
print("BMI:",bmi)

if bmi<= 20:
    print("you are fail!")
elif bmi <= 35:
    print("you are pass!")
elif bmi <= 45:
     print("you are below average!")
elif bmi <= 70:
     print("you are you are above average!")
elif bmi <= 80:
      print("you are excellent!")
else:
      print("you are oustanding!")

      


    
