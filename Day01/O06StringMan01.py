
# strings

st = "Hello World"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st :{st}")
print(f"st[0]  :{st[0]}")            # strings are stored like arrays
print(f"st[6]  :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing - use the indexes and extract a part of the string
print("-" * 60)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

# python supports reverse indexing
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 60)
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[::-1]      :{st[::-1]}")

# plindrome
print("-" * 60)
st1 = "malayalam"
print("Palindrome" if st1[:] == st1[::-1] else "Not a Palindrome")

# strings are immutable
print("-" * 60)
st = "hello world"
print(f"st :{st}")
print(f"st[0] :{st[0]}")
# st[0] = "H"

print("replace".center(60, "-"))
# print(dir(st))

print(f"st :{st}")
res = st.replace("h", "H")
print(f"res :{res}")

print("-" * 60)

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st[0:6] + st[6:].replace("l", "L")
print(f"res :{res}")

print("-" * 60)
print(f"st :{st}")

res = st.find("w")
print(f"res :{res}")

res = st.find("l")
print(f"res :{res}")

print("-" * 60)

res = st.find("l", 6, 11)  # hard coding
print(f"res :{res}")

print("-" * 60)

res = st.find("l", st.find("l") + 1)
print(f"res :{res}")

print("-" * 60)
st = "hello word"
res = st.find("l", st.find("l", st.find("l") + 1) + 1)
print(f"res :{res}")


