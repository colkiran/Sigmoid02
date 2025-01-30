
def outerFun(gname):
    def innerFun():

        print(f"Greetings Mr.{gname}, Welcome to the event")

    return innerFun

outerFun("Sachin")()

print("-" * 60)

inref = outerFun("Rahul")

print("Hello World \n" * 5)

inref()         # lost the scope of outerFun

