
def outerFun():

    def innerFun():

        print("Hello World")

    return innerFun

outerFun()()            # calls the innerFun()

print("-" * 60)
inref = outerFun()

# some code
print("Hai \n" * 10)


inref()                 # calls the innerfun()



