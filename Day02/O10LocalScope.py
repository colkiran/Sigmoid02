
def fun(x):         # x is a local var
    print(f"inside :{x}")
    y = "hello world"   # y is also a local var
    print(f"inside :{y}")

fun(50)

# print(f"outside :{x}")
# print(f"outside :{y}")