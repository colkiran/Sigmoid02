from functools import total_ordering

@total_ordering   # you should have overloaded == and one more compaison operator
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # it works for not equal
    def __eq__(self, other):
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Jack", 7000)
# emp1.get_details()
emp2 = Employee("Jill", 6000)
print("-" * 60)
print(str(emp1))

print("-" * 60)
print(emp1)       # it will implicitly call __str__

print("-" * 60)
if emp1.salary != emp2.salary:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)
print(emp1 < emp2)

print("-" * 60)
print(emp1 >= emp2)
