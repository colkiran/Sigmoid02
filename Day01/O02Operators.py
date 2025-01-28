"""
1. arithmetic
2. comparison or relational
3. logical
4. Bitwise
5. Ternary
"""

print("Arithmetic Operators".center(60, "-"))
print(f"10 + 3 = {10 + 3}")     # add
print(f"10 - 3 = {10 - 3}")     # sub
print(f"10 * 3 = {10 * 3}")     # mul
print(f"10 / 3 = {10 / 3}")     # div
print(f"10 // 3 = {10 // 3}")   # floor div
print(f"10 % 3 = {10 % 3}")     # modulus
print(f"10 ** 3 = {10 ** 3}")   # exponential

print("Augmentor Operator".center(60, "-"))
#  =, +=, -=, *=, /=
x = 10
print(f"x :{x}")
x += 5
print(f"x :{x}")
x /= 3
print(f"x :{x}")

print("Comparison".center(60, "-"))
# ==, >, <, >=, <=, !=
a = 10
b = 20
print(f"a == b :{a == b}")
print(f"a != b :{a != b}")
print(f"a < b :{a < b}")
print(f"a > b :{a > b}")

print("Logical Operators".center(60, "-"))
# and, or, not

print(f"1 == 1 and 1 == 1 :{1 == 1 and 1 == 1}")
print(f"1 == 2 and 1 == 1 :{1 == 2  and 1 == 1}")

print("-" * 60)

print(f" 1 == 1 or 1 == 1 :{1 == 1 or 1 == 1}")
print(f" 1 == 1 or 2 == 1 :{1 == 1 or 2 == 1}")

print("-" * 60)

print(f" not(1 == 1 or 1 == 1) :{not(1 == 1 or 1 == 1)}")
print(f" not(1 == 1 or 2 == 1) :{not(1 == 1 or 2 == 1)}")

print("-" * 60)

print(f"ord('a')  :{ord('a')}") # integer representation of unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(60, "-"))
print(f"5 | 3 :{5 | 3}")
print(f"5 & 3 :{5 & 3}")
print(f"5 ^ 3 :{5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

# ternary operator
age = 10
print("Eligible" if age > 17 else "Not Eligible")
