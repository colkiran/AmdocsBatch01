
emp = {'emp1' :{'name': 'Mike', 'age': 29, 'dept': 'finance', 'desig':'MGR', 'location': 'blr'},
       'emp2' :{'name': 'Tanya', 'age': 32, 'dept': 'HR', 'desig':'GM', 'location': 'hyd'},
       'emp3': {'name': 'steve', 'age': 30, 'dept': 'MKT', 'desig':'BDM', 'location': 'del'}
       }

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
       print(ky)
       print("-" * len(ky))
       for k, v in info.items():
              print(k, "=>", v)
       print("-" * 40)

print("update".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 29, 'dept': 'finance', 'desig':'MGR'}
emp2 = {'name': 'Tanya', 'age': 32, 'dept': 'HR',  'location': 'hyd'}
print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")


print("-" * 40)
emp1.update(emp2)

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

print("copy".center(40, "-"))
emp1 = {'name': 'Mike', 'age': 29, 'dept': 'finance', 'desig':'MGR', 'location': 'blr'}
print(f"emp1 Before :{emp1}")

emp2 = emp1                 # shallow copy - copies the address along with the data

print(f"emp2 Before :{emp2}")
emp2['gender'] = 'male'
emp2['salary'] = '85000'

print(f"emp2 After :{emp2}")
print(f"emp1 After :{emp1}")

print("=" * 40)
emp3 = {'name': 'Tanya', 'age': 32, 'dept': 'HR', 'desig':'GM', 'location': 'hyd'}
print(f"emp3 before :{emp3}")

emp4 = emp3.copy()

print(f"emp4 before :{emp4}")
emp4['sal'] = 60000
emp4['con'] = 90349233353

print(f"emp4 After :{emp4}")
print(f"emp3 After :{emp3}")

print("=" * 40)

emp5 = {'name': 'steve', 'age': 30, 'dept': 'MKT', 'desig':{'hp': 'trainee', 'wipro': 'executive', 'IBM': 'BDM'}, 'location': 'del'}
print(f"emp5 Before :{emp5}")

emp6 = emp5.copy()

print(f"emp6 Before :{emp6}")
emp6['desig']['midtree'] = 'GM'
emp6['desig']['deloite'] = 'VP'

print("-" * 40)
print(f"emp6 After :{emp6}")
print(f"emp5 After :{emp5}")

print("=" * 40)

emp7 = {'name': 'steve', 'age': 30, 'dept': 'MKT', 'desig':{'hp': 'trainee', 'wipro': 'executive', 'IBM': 'BDM'}, 'location': 'del'}

from copy import deepcopy

emp8 = deepcopy(emp7)

print(f"emp8 Before :{emp8}")

emp8['desig']['midtree'] = 'GM'
emp8['desig']['deloite'] = 'VP'

print(f"emp8 After :{emp8}")
print(f"emp7 After :{emp7}")