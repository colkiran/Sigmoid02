
def fun(x):
    print(f"Inside :{x}")
    x = 100
    print(f"Modified val of x :{x}")


y = 50
print(f"Before  :{y}")

fun(y)

print(f"After :{y}")