
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player initialized.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 56)
ply2 = Player("Virat", 36)

print("-" * 60)
ply1.get_details()
ply2.get_details()

print("-" * 60)
ply2.runs = 65
print(ply2.runs)

print("-" * 60)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 60)
# self will have the name of the object that made a call to the method
# ply1.get_details()   -> self - ply1
