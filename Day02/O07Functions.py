
def greet():
    print("Greetings Mr. Sachin, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event....")

# city as default argument and gname as non default argument
def greetGstCty(gname, city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")

greet()

print("-" * 60)
greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")   # keyword arg

print("-" * 60)
# kword args

def admsn(fname, lname, dob, place, gender, qlf, conno, adhrno):
    print(f"Name :{fname + lname}")
    print(f"dob :{dob}")
    print(F"place :{place}")
    print(f"Gender :{gender}")
    print(f"Qualification :{qlf}")

    # kwargs
admsn(lname = "Tendukar", place = "Mumbai", qlf="graduate", fname='sachin', conno = "2893749234", adhrno="SFWE34534WTE", dob="12/10/1971", gender="Male")

# args
admsn('Rahul', 'Dravid', '12/10/1972', "Bangalore", "Male",  "graduate",  "3434234", "2352 7834 A34E")

print("-" * 60)
# variable length argument

def productAll(*numbers):
    print(*numbers)     # unpack
    print(numbers)
    prod = 1
    for num in numbers:
        prod *= num
    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def extract_details(**detail):
    print(detail)
    for k, v in detail.items():
        print(k + " => " + str(v))

extract_details(name="Sachin", age=36, runs=120, oppn="WI")

print("-" * 60)
# functions can return values

def mulMe(x):
    return x * x

print(mulMe(8))

print("-" * 60)

def ArithmeticCal(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

print(ArithmeticCal(20, 8))

print("-" * 60)
# doc string

def fun():
    "This is a doc string"
    # This is a comment
    print("hello world.....")

fun()

print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1 takes two arguments x and y

    1. if x and y are integers the fun1 returns the sum of the intergers
    2. if x and y are strings the fun1 returns the concatenated string of fun1 and fun2
    3. if x and y are of two different data types then throws an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))
# print(fun1("hello", 100))

print("-" * 60)

help(fun1)
