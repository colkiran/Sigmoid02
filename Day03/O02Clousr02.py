

def outerFun(greet):
    # simple curry
    def innerFun(gname):
        print(greet, gname)

    return innerFun

engGreet = outerFun("Hello")
hndGreet = outerFun("Namaskar")

engGreet("Virat")
hndGreet("Jadeja")

