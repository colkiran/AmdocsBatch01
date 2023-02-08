
# append, insert, extend

print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")
print(l1[8][1:4])

print("extend".center(40, "-"))
l2 = [10, 20, 30, 40, 50]
print(f"l2 :{l2}")

l2.extend([60, 70, 80, 90, 100])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = [1, 2, 3, 4, 5]
print(f"l3 :{l3}")

l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)

print(f"l3 :{l3}")

# remove values from a list - pop, remove, clear
print("pop".center(40,"-"))
l1 = list(range(2, 20, 2))
print(f"L1 :{l1}")

res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop(5)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 3, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3]
print(f"l1 :{l1}")
l1.remove(1)
l1.remove(2)
l1.remove(3)
# l1.remove(5)

print(f"l1 :{l1}")

print("clear".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("index".center(40, "-"))
l1 = [1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1]
print(f"l1 :{l1}")
print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3) + 1))
print("3 :", l1.index(3, l1.index(3, l1.index(3) + 1) + 1))
