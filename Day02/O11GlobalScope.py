
glbX = 100

def fun(x):     # x is a local var
    global glbX
    print(f"inside local :{x}")
    # print(glbX)
    # glbX = 50           # local variable with the same name as a global var
    glbX = 50
    print(f"inside :{glbX}")

print(f"Before :{glbX}")

fun(15)

print(f"After :{glbX}")
