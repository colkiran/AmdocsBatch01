
"""
sort    -   will sort the original list
sorted  -   will take a copy of the list and sort it
"""

print(f"sort".center(40, "-"))
l1 = [8, 5, 1, 9, 2, 10, 4, 6, 3, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending Order :{res_desc}")

print("-" * 40)
l1 = [8, 'zebra', 5, 'apple', 1, 'yellow', 9, 'red',2, 'violet',  10, 'pink', 4, 'green',  6, 'blue',  3, 'orange', 7, 19, 124, 1089, 26, 210, 2431]

print(f"l1 :{l1}")

print("-" * 40)
res =sorted(l1, key=ascii)
print(f"res :{res}")
