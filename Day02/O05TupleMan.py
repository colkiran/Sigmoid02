
# tuples

t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)
t2 = (1, 2, 3, 4.5, 5.2, 6.0, 7+3j, 8-2j, 'nine', 'ten', True, False)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 6))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t1 = (1, 2, 3, 4, 5)
print(f"t1 :{t1}")
# t1[2] = 300

print("-" * 60)
# print(dir(t1))

t1 = (1, 1, 2, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2)
print(f"t1 :{t1}")

print("count".center(60, "-"))
print(f"t1 :{t1}")
print(f"count of 1 :{t1.count(1)}")
print(f"count of 2 :{t1.count(2)}")
print(f"count of 3 :{t1.count(3)}")
print(f"count of 5 :{t1.count(5)}")

print("index".center(60, "-"))
print(t1.index(3))
print(t1.index(3, t1.index(3) + 1))
print(t1.index(3, t1.index(3, t1.index(3) + 1) + 1))


