
print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1         # shallow copy - copy the address with the data
print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")

# copy the list l3 tp l4
l4 = l3.copy()      # deep copy - copies only the data
print(f"l4 before :{l4}")

l4.extend([11, 12, 13])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
l5 = [2, 4, 6, [1, 2, 3, 4, 5],  8, 10]
print(f"l5 before :{l5}")

# copy list l5 to l6
l6 = l5.copy()
print(f";6 before  :{l6}")
l6[3].append(6)
l6[3].append(7)
l6[3].append(8)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
l7 = [1, 2, 3, [10, 20, 30, 40, 50], 4, 5]
print(f"l7 before :{l7}")

# copy list l7 to l8
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[3].extend([60, 70, 80])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")

print("sort".center(60,  "-"))
l1 = [3, 7, 9, 5, 10, 2, 1, 6, 4, 8]
print(f"l1 :{l1}")

res_asc = sorted(l1)
res_desc= sorted(l1, reverse=True)
print(f"Ascending order :{res_asc}")
print(f"Descendng order :{res_desc}")

print("-" * 60)
l1 = [3, 'zebra', 'apple',  7, 'yellow', 'blue',  9, 'white', 'xray', 5, 'green', 'maroon',  10, 'pink', 'violet', 2, 'orange', 'cat', 1, 'fish', 6,'dog', 4, 'elephant', 8, 189, 1234, 29, 275, 2034]
print(f"l1 :{l1}")

res_asc = sorted(l1, key=ascii)
print(res_asc)

for i in range(0, len(res_asc)):
    if type(res_asc[i]) == int:
        print(i)
        break
print(res_asc[:15] + sorted(res_asc[15:]))







