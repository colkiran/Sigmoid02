d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print('-' * 60)
d2 = {'name': 'Sachin', 'age': 36, 'runs': 125, 'oppn': 'Aus'}
print(f"d2 :{d2}")
print(type(d2))

print('-' * 60)
d3 = dict([('name', 'Rahul'), ('age', 35), ('runs', 85), ('oppn', 'SA')])
print(f"d3 :{d3}")

print('-' * 60)
d4 = dict(name='dhoni', age=36, runs=102)
print(f"d4 :{d4} ")
print(type(d4))

print('-' * 60)
# CRUD

player = {'name': 'Sachin', 'age': 36, 'runs': 85, 'oppn': 'Aus'}
print(f"players :{player}")

# read
print(f"Name :{player['name']}")
print(f"Age : {player['age']}")
print('-' * 60)

for i in player:
    print(i, "=>", player[i])

# update - modify and add
print('-' * 60)
print(f"player :{player}")

# modification
player['name'] = 'Tendulkar'
player['runs'] = 98
print(f"Player :{player}")

player['venue'] = 'Perth'
player['year'] = 2008

print(f"player :{player}")

# delete
del player['age']
del player['oppn']

print(f"player :{player}")

print('-' * 60)
print(dir(player))

print("fromkeys".center(60,  "-"))
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")
print(type(cities))

res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 23)
print(f"res :{res}")

print("setdefault".center(60, "-"))
emp = {'name': 'Kevin', 'age': 35, 'desig': 'MGR', 'dept': 'Finance'}
print(f"enp :{emp}")

emp.setdefault('age', 45)
emp.setdefault('desig', 'Director')
emp.setdefault('loc', 'Blr')
emp.setdefault('salary', 145000)
print(f"emp :{emp}")

print("keys".center(60, "-"))
emp = {'name': 'Kevin', 'age': 35, 'desig': 'MGR', 'dept': 'Finance'}
print(f"enp :{emp}")

k = emp.keys()
print(f"keys :{k}")
print('-' * 60)

for k in emp.keys():
    print(k, "=>", emp[k])

print("get".center(60, "-"))
emp = {'name': 'Kevin', 'age': 35, 'desig': 'MGR', 'dept': 'Finance'}
print(f"enp :{emp}")

print(f"Designation :{emp.get('desg', 'Invalid Key, Please enter a valid one....')}")

print("update".center(60, "-"))
emp1 = {'name': 'Kevin', 'age': 35, 'desig': 'MGR', 'dept': 'Finance'}
print(f"enp1 :{emp1}")

emp2 = {'name': 'Peter', 'age': 25, 'loc': 'blr', 'sal': 125000}
print(f"enp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(60, "-"))
emp2 = {'name': 'Peter', 'age': 25, 'loc': 'blr', 'sal': 125000}
print(f"enp2 :{emp2}")

emp2.clear()
print(f"emp2 :{emp2}")

emp2 = {'name': 'Peter', 'age': 25, 'loc': 'blr', 'sal': 125000}
for k, v in emp2.items():
    print(k, "=>", v)

