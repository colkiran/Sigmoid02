

class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.age = 1
    def eat(self):
        print("Animal eat....")
class Bird(Animal):

    def __init__(self):
        super().__init__()
        print("Bird Ctor.....")
        self.weight = '1 kg'

    def fly(self):
        print("Birds fly.....")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print(cuckoo.__dict__)
