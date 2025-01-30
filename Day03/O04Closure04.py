
def fun(*args):
    print(args,"\t", *args)
    print("-" * 60)

fun()
fun(1)
fun(1, 2)
fun(1, 2, 3)
fun(1, 2, 3, 4)
fun(1, 2, 3, 4, 5)

def sum(x, y):
    print(f"sum of {x} and {y}")
    return x + y

def diff(x, y):
    print(f"difference of {x} and {y}")
    return x - y

# HOF - Higher order function - if a function takes a function as an argument or returns a function as a return value

def log_detials(fnc):
    logInfo = "Logging into the service"

    def innerFun(*args):
        print(logInfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sum_logger = log_detials(sum)
diff_logger = log_detials(diff)

sum_logger(35, 77)
diff_logger(97, 76)


