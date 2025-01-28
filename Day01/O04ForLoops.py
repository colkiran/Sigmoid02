
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)
# continue - skip the current iteration
# break - stop the iteration
# else

for i in range(1, 31):
    # if i >= 25:
    #     break;
    if i % 2 == 1:
        continue           # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted generating numbers.....")


