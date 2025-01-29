print("Conversion".center(60, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3698234982374))
print("The number {num:5} {num:f} {num:b}".format(num=36))

print("Alignment".center(60, "-"))
print("{num:15} Tendulkar".format(num="Sachin"))
print("{num:15} Tendulkar".format(num=36))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("Alignment".center(60, "-"))
print("{val:>15} Tendulkar".format(val="Sachin"))       # right
print("{val:^15} Tendulkar".format(val="Sachin"))       # Center
print("{val:<15} Tendulkar".format(val="Sachin"))       # left

print("{num:10.2f}".format(num=pi))
print("{num:010.2f}".format(num=pi))
print("{num:010.3f}".format(num=pi))
print("{num:010.4f}".format(num=pi))

print("{val:-^60}".format(val="Formatting"))
print("formatting".center(60, "-"))

print("-" * 60)
print("{0:10.2f}\t{1:10.2f}".format(pi, -pi))

print("{0:10.2f}\t{1:=010.2f}".format(-pi, -pi))
print("{0:10.2f}\t{1:=10.2f}".format(-pi, -pi))








