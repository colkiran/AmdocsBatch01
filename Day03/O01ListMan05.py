
"""
reverse     -   reverse the original list
reversed    -   reversed will return a copy of reversed list
"""
l1 = [9, 5, 6, 10, 3, 8, 1, 4, 2, 7]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")

#sorted
print("sorted".center(40, "-"))

cities = ['thiruvananthapuram', 'ooty', 'bangalore', 'delhi', 'hyderabad', 'vishakapatnam', 'pune', 'kanyakumari', 'chennai', 'kolkota', 'mumbai']
print(f'cities :{cities}')

print("-" * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)
months = ['aug', 'dec', 'apr', 'nov', 'jul', 'oct', 'jan', 'sep', 'feb', 'may', 'jun', 'mar']
print(f"months :{months}")

from calendar import month_abbr
print(list(month_abbr))
l = []
for month in list(month_abbr):
    l.append(month.lower())
print(f"l :{l}")

def sort_month(mon):
    if mon in l:
        return l.index(mon)

print("-" * 40)
res_asc = sorted(months, key=sort_month)
print(f"res_asc :{res_asc}")

print("-" * 40)
res_desc = sorted(months, key=sort_month, reverse=True)
print(f"res_desc :{res_desc}")

print("-" * 40)
res = sorted(months, key=list(map(lambda mon: mon.lower(), list(month_abbr))).index)
print(f"res :{res}")



