
print("Arithmetic Operators")
print(f"Add :10 + 3 = {10 + 3}")
print(f"Sub :10 - 3 = {10 - 3}")
print(f"Mul :10 * 3 = {10 * 3}")
print(f"Div :10 / 3 = {10 / 3}")
print(f"floor :10 // 3 = {10 // 3}")
print(f"Mod :10 % 3 = {10 % 3}")
print(f"Exp :10 ** 3 = {10 ** 3}")

print("Augmentor".center(40, "-"))
#  =, +=, -=, /=, *=
x = 10
print(f"x :{x}")

x += 5          # x = x + 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
#  == , >, >=, <, <=, !=
a = 10
b = 15
print(a > b)
print(a < b)
print(a == b)
print(a != b)

print("Logical Operators".center(40, "-"))
# and, or, not

print(1 == 1 and 2 == 2)
print(1 == 1 and 1 == 2)

print(1 == 1 or 2 == 2)
print(1 == 1 or 1 == 2)

print(not(1 == 1 or 2 == 2))
print(not(1 == 1 or 1 == 2))

print("-" * 40)
print(f'ord("A") :{ord("A")}')      # integer representation of unicode                                     character
print(f"ord('Z') :{ord('Z')}")
print(f"ord('a') :{ord('a')}")
print(f"ord('z') :{ord('z')}")

print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operator".center(40, "-"))
print(f"5 | 3 = {5 | 3}")
print(f"5 & 3 = {5 & 3}")
print(f"5 ^ 3 = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"8 << 1 = {8 << 1}")
print(f"5 << 2 = {5 << 2}")
print(f"16 >> 1 = {16 >> 1}")
print(f"5 >> 1 = {5 >> 1}")             # 101 >> 10 => 2

# Ternary Operator
age = 20
print("Eligible" if age >= 18 else "Not Eligible")

