
from abc import ABC, abstractmethod

class Account(ABC):

    def deposit(self):
        pass
    @abstractmethod
    def get_balance(self):
        pass

class Savings(Account):

    def get_balance(self):
        print("balance is ########")
    def withdraw(self):
        print("Amount debited.......")

sav1 = Savings()
sav1.get_balance()
sav1.withdraw()
