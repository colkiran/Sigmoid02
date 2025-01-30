
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player initialized.....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fn, ln, age):
        print("Factory...")
        return cls(f"{fn} {ln}", age)      # calls the constructor

    @staticmethod
    def add(x, y):
        print(x + y)


ply1 = Player("Virat", 36)
ply1.get_details()

print("-" * 60)
ply2 = Player.createPlayer("Rohit", "Sharma", 38)
ply2.get_details()

print("-" * 60)
Player.add(34, 94)
