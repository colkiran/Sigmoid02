
def fun(lst):
    print(f"Inside before :{lst}")
    lst.extend([6, 7, 8, 9, 10])
    print(f"Inside after :{lst}")

l1 = list(range(1, 5))
print(f"before call :{l1}")

fun(l1)

print(f"after call :{l1}")
