
def callMe():
    print(f"Apples from Ooty")


def fun(fnc):
    print("Hello")
    fnc()
    print("hi")
    print('_' * 40)

    def defineMe():
        print(f"Oranges from Kanpur")
    return defineMe


def funCallback(fnc):
    print("Mera Bharath Mahan")
    fnc()
    print("India is great")


funCallback(fun(callMe))
