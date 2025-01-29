
s1 = set()
print(F"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 5.1, 6.5, 7.9, 8.0, 9+2j, 10-3j, 'eleven', 'twelve', 'thirtee', 'fourteen', True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 6))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
# add, update, pop, discard, remove

s1 = {1, 2, 3}
print(f"s1 :{s1}")

s1.add(4)
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)

print(f"s1 :{s1}")

# update
s1.update([1, 2, 3])
s1.update([4, 5, 6])
s1.update([3, 4, 5])
s1.update([7, 8, 9])
s1.update([10, 8, 3])

print(f"s1 :{s1}")

print("-" * 60)
# pop
res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")
print("-" * 60)
# remove

s1.remove(6)
s1.remove(8)
# s1.remove(1)
print(f"s1 :{s1}")

print("-" * 60)
# discard

s1.discard(4)
s1.discard(10)
s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 60)
# frozen sets - immutable

fs = frozenset([1, 2, 3, 4, 5])
print(f"fs :{fs}")
print(type(fs))


