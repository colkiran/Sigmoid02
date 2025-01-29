l1 = list()
print(F"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5.6, 6.1, 7.9, 8.0, 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 14+2j, 15-5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = list(range(1, 6))
print(f"l1 :{l1}")

# CRUD
# read
print("-" * 60)
print(f"l1 :{l1}")
for i in l1:
    print(i, end=" ")
print()

# update  1. modify the data, 2. add a new element
# modify
print(f"l1 :{l1}")
print(f"l1[2] :{l1[2]}")
l1[2] = 300
print(f"l1 :{l1}")

# add new value
l1[4] = 4.5
print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))

print("append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)
print(f"l1 :{l1}")
l1.append([10, 11, 12, 13, 14])
print(f"l1 :{l1}")

print("extend".center(60, "-"))
l2 = [10, 20, 30, 40, 50]
print(f"l2 :{l2}")
l2.extend([60, 70, 80, 90])
print(f"l2 :{l2}")
l2.extend([100])
print(f"l2 :{l2}")

print("remove".center(60, "-"))
l1 = list(range(2, 13, 2))
print(f"l1 :{l1}")
l1.remove(8)
l1.remove(4)
# l1.remove(1)
print(f"l1 :{l1}")

print("pop".center(60,  "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")
res = l1.pop(7)
print(f"res :{res}")
res = l1.pop(3)
print(f"res :{res}")
# res = l1.pop(9)
# print(f"res :{res}")

print(f"l1 :{l1}")







