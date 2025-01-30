
def funLogger(fnc):

    def helper(x):
        print("Logging into the service.....")
        fnc(x)
        print("logged out the service......")
        print("-" * 60)

    return helper

def deposit(amt):
    print(f"Amount {amt} credited successfully into the account.....")

funLogger(deposit)      # no output
print("-" * 60)

funLogger(deposit)(5000)
print("-" * 60)

res_fun = funLogger(deposit)
res_fun(5000)
print("-" * 60)

deposit = funLogger(deposit)
deposit(5000)     # calls the helperFun
print("-" * 60)

@funLogger    #  withdraw = funlogger(withdraw)
def withdraw(amt):
    print(f"Amount {amt} debited successfully from the account.....")

withdraw(1500)




