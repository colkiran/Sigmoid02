
def add(x, y):
    return x + y

# print(add(10, 20))

a = add
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)

l = lambda i, j : i + j
res = l(27, 56)
print(f"res :{res}")

"""
lambdas are best used with 
  a. map
  b. filter 
  c. reduce
"""

print("map".center(60, "-"))

lst = list(range(1, 11))
print(f"lst :{lst}")

squares = list(map(lambda x : x ** 2, lst))

print(f"squares :{squares}")

print("Filter".center(60, "-"))
l1 = list(range(1, 31))
print(f"l1 :{l1}")

even_num = list(filter(lambda x :  x % 2 == 0, l1))
print(f"even numbers :{even_num}")

print("-" * 60)

sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

res = list(filter(lambda word : word != 'the', sentence.split()))
print(f"res :{res}")

res = list(filter(lambda word : len(word) == 3, sentence.split()))
print(f"res :{res}")

print(f"reduce".center(60, "-"))
from functools import reduce

l1 = list(range(1, 11))
l2 = [8, 4, 7, 2, 9, 5, 6, 3]


res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

res = reduce(lambda x, y: x if x > y else y, l2)
print(f"res :{res}")

res = reduce(lambda x, y: x if x < y else y, l2)
print(f"res :{res}")

