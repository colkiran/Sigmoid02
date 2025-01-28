
"""
maketrans
translate

will convert every byte using a dictionary.
dictionary will have the character and its ascii value stored
"""

print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")

# length of a and b should be the same
a = "helowrd"
b = "HELOWRD"

res_tbl = st.maketrans(a, b)
print(f"res_tbl :{res_tbl}")

res = st.translate(res_tbl)
print(f"res :{res}")

# C Style of formatting printf
print("format".center(60, "-"))
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")       # tuple
print(values)
print(format % values)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.346546, "class"))
print(format % ("Sachin", 4.8781263, "class"))
print(format % ("Sachin", 4.8765, "class"))

print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.788898, "class"))

print("-" * 60)
# unix style
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
print(tmpl.substitute(name= "Sachin", adj="class"))

print("-" * 60)
# format strings of python
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))

print("Welcome {2}, what a {0} player for {1}".format("Sachin", "class", "India"))

print("Welcome {name}, with a rating of {rat:.3f}, what a {adj} player".format(name="Sachin", adj="class", rat=4.7999999))

# interpolation
print("-" * 60)
from math import pi, e
print(f"The value of pi={pi} and Eulers constant = {e}")

print("PI = {} and Eulers Constant = {}".format(pi, e))
print("PI = {}, Eulers Constant = {} and magic_number = {magic}".format(pi, e, magic=40585))

print("PI = {0}, Eulers Constant = {1} and magic_number = {magic}".format(pi, e, magic=40585))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']
print(full_name)

print("Mr. {name}".format(name=full_name))
print("Mr. {name[0]} {name[1]}".format(name = full_name))


