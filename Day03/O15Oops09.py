
class Animal:
    def eat(self):
        print("Animals eat....")

class Bird(Animal):
    def fly(self):
        print("Birds fly")

class Chicken(Bird):

    def fly(self):
        print("Chickens seldom fly.....")

chic = Chicken()
chic.eat()
chic.fly()
