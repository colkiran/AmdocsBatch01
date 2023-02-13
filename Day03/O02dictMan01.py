
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 40)
d2 = {'name': 'sachin', 'age': 34, 'runs': 145, 'oppn': 'Aus', 'venue': 'Perth'}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 40)
d3 = dict([('name', 'sachin'), ('age', 34), ('runs', 145), ('oppn', 'Aus'), ('venue', 'perth')])
print(f"d3 :{d3}")
print(type(d3))

print('-' * 40)
d4 = dict(name='rahul', age=32, runs=85, oppn='england', venue='lords')
print(f"d4 :{d4}")
print(type(d4))

print('-' * 40)
player = {'name': 'Sachin', 'age': 32, 'runs': 125, 'oppn': 'West Indies', 'venue': 'Sabina Park'}
print(f"player :{player}")
print('-' * 40)

print(f"Name     :{player['name']}")
print(f"Runs     :{player['runs']}")
print(f"opponent :{player['oppn']}")

print('-' * 40)
# iterating

for i in player:
    print(i, "=>", player[i])

# modify or update
print('-' * 40)
player['age'] = 30
player['runs'] = 50
player['venue'] = 'chepauk'
player['year'] = 2001

print(f"player :{player}")

# delete
print('-' * 40)
del player['venue']
del player['age']
del player['runs']

print(f"player :{player}")

# print('-' * 40)
# print(dir(player))

print("keys".center(40, "-"))
player = {'name': 'Sachin', 'age': 30, 'runs': 50, 'oppn': 'West Indies', 'venue': 'chepauk', 'year': 2001}

print("-" * 40)
print(f"player :{player}")
k = player.keys()
print(f"k :{k}")

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
print(f"player :{player}")

print("-" * 40)
res = player.values()
print(f"res :{res}")