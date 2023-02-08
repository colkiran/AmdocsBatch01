
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.2, 8.1, 9.5, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values: {values}")

a, b, *c = values          # variable with a * can store more than one value
print(a, b, c, sep=", ")

a, *b, c = values
print(a, b, c, sep=", ")
print(b[3])

*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")

lst4 = [*lst1, *lst2]
print(len(lst4))
print(f"lst4 :{lst4}")
