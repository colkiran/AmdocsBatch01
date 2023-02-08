
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
print(f"st[0] :{st[0]}")        # strings are stored like list
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 40)
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

print("-" *  40)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" *  40)
# slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:12:-1]  :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")


print("-" * 40)
# write a code to find the given string is a palindrome
st = "malayalam"
if (st[:] == st[::-1]):
    print(f"The string is a palindrome :{st}")
else:
    print(f"The string is NOT a palindrome :{st}")

print("-" * 40)
# strings are immutable
st = "hello"
print(f"st :{st}")
print(st[0])
# st[0] = "H"

print("find".center(40, "-"))
# print(dir(st))

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

pos = st1.find("l")
print(f"pos :{pos}")

pos = st1.find("l", st1.find("l") + 1)
print(f"pos :{pos}")

pos = st1.find("l", st1.find("l", st1.find("l") + 1) + 1)
print(f"pos :{pos}")

pos1 = st2.find("the")
print(f"pos1 :{pos1}")

pos1 = st2.find("the", st2.find("the") + 1)
print(f"pos1 :{pos1}")
