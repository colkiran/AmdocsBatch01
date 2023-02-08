
for i in range(1, 11):
    print(i, end=" ")
print()

# continue, break, else

for i in range(1, 30):
    # if i > 20:
    #     break               # come out of the iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted the iteration......")