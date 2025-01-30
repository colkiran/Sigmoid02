
from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")


class Developer(Employee):

    def doJob(self):
        print("do coding.......")


def BankJob(emp):
    print("Bank Job Started......")
    emp.doJob()
    print("Bank Job Ended.......")
    print("-" * 60)

Mark = Manager()
David = Developer()

BankJob(Mark)
print("-" * 60)
BankJob(David)
