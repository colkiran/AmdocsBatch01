
print("replace".center(40, "-"))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

res = st1.replace("h", "H")
print(f"res :{res}")

res = st1.replace("l", "L", 1)
print(f"res :{res}")

res = st2.replace("the", "The", 1)
print(f"res :{res}")

res = st2.replace("fox", "tiger")
print(f"res :{res}")

# maketrans, translate
print("maketrans".center(40, "-"))
st = "hello world"
print(f"st :{st}")
a = 'helowrd'
b = "HELOWRD"
# Length of a and b should be same
transTbl = st.maketrans(a, b)
print(transTbl)

print("translate".center(40, "-"))
res = st.translate(transTbl)
print(f"res :{res}")

print("strip".center(40, "-"))
st = "********hello*********"
print(f"st :{st}")

#lstrip
res = st.lstrip("*")
print(f"res :{res}")

#rstrip
res = st.rstrip("*")
print(f"res :{res}")

res = st.strip("*")
print(f"res :{res}")
