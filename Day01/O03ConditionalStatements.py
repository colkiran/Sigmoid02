x = int(input("Enter the first value :"))
if x < 10: print(f"x is a single digit number :{x}")

y = int(input("Enter the second number :"))
z = int(input("Enter the third number :"))

if x >= y and x >= z :
    print(f"x is the greatest :{x}")
elif y >= x and  y >= z :
    print(f"y is the greatest :{y}")
else:
    print(f"z is the greatest :{z}")

print("-" * 60)

age = 22
if (age >= 18 and age <= 65) :
    print("Eligible.....")
else:
    print("Not Eligible.....")

print("-" * 60)

# mathematical equation
if (18 <= age <= 65):
    print("Eligible....")
else:
    print("Not Eligible....")
