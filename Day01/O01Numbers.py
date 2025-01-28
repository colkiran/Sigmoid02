
"""
int
float
complex

called as f string or format string
print(f"a :{a}")

used for interpolation - printing the value of a variable inside double quotes

"""

a = 1
b = -1
print(f"a: {a}")
print(f"type(a): {type(a)}")    # RTTI - Run Time Type Identification
print(f"b :{b}")
print(f"type(b): {type(b)}")

print("-" * 60)
c = 1.0
d = -2.0
print(f"c :{c}")
print(f"type(c) :{type(c)}")
print(f"d :{d}")
print(f"type(d) :{type(d)}")

print("-" * 60)
e = +2e3
f = -2e3
print(f"e :{e}")
print(f"type(e) :{type(e)}")
print(f"f :{f}")
print(f"type(f) :{type(f)}")

print("-" * 60)
g = 3.14j
h = -3.14j
print(f"g :{g}")
print(f"type(g) :{type(g)}")
print(f"h :{h}")
print(f"type(h) :{type(h)}")

print("-" * 60)
res = 2 + 3.5
print(f"res :{res}")
print(f"type(res) :{type(res)}")

x = 2
y = 3.5
z = x + y
print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("Conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)       # decimal
print(0b11)     # binary
print(0b101)    # binary
print(0o11)     # octal
print(0o101)    # octal
print(0xe)      # hexa
print(0xa)      # hexa

print("Number System Conversion".center(6, "-"))
x =100
print(f"bin(x) :{bin(x)}")
print(f"hex(x) :{hex(x)}")
print(f"oct(x) :{oct(x)}")
