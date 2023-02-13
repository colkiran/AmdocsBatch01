
player = {'name': 'Sachin', 'runs': 50, 'oppn': 'West Indies', 'venue': 'chepauk', 'year': 2001}

print(f"player :{player}")
print("-" * 40)

print(f"Year :{player.get('year', 'please enter a valid key')}")
print(f"Age  :{player.get('age', 'please enter a valid key')}")

print("fromkeys".center(40, "-"))
cities =  ['blr', 'che', 'mum', 'hyd', 'del', 'kol', 'pun']
print(f"cities :{cities}")

print("-" * 40)
res1 = dict.fromkeys(cities)
print(F"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")


print("setdefault".center(40, "-"))
player = {'name': 'Sachin', 'runs': 50, 'oppn': 'West Indies', 'venue': 'chepauk'}
print(f"player :{player}")

print("-" * 40)
player.setdefault('runs', 150)
player.setdefault('age', 32)
player.setdefault('oppn', 'South Africa')
player.setdefault('year', 1998)

print(f"player :{player}")

print("pop".center(40, "-"))

player  = {'name': 'Sachin', 'runs': 50, 'oppn': 'West Indies', 'venue': 'chepauk', 'age': 32, 'year': 1998}
print(f"player :{player}")

res  = player.pop('year')
print(res)

res = player.pop('oppn')
print(res)

print(f"player :{player}")

print("popitem".center(40, "-"))
player  = {'name': 'Sachin', 'runs': 50, 'oppn': 'West Indies', 'venue': 'chepauk', 'age': 32, 'year': 1998}
print(f"player :{player}")

print("-" * 40)
res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print("-" * 40)
print(f"player :{player}")
