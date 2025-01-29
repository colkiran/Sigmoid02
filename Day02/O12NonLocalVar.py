
def outerFun():
    gstname = "Sachin"          # local variable

    def innerFun():

        nonlocal gstname        # only local var can be converted to nonlcl
        print("Hello World")
        gstname += " Tendulkar"
        print(f"Greetings Mr.{gstname}")

    # outerfun scope
    innerFun()
    print(f"From outerFun :{gstname}")

outerFun()