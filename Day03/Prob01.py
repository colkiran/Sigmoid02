
import time
def calc_time(fnc):   

    def helper(x):
        print("Logging into the server")
        st=time.perf_counter()
        fnc(x)
        et=time.perf_counter()
        print(f"The time taken by the function to execute is : {round(et-st,2)}")
        print("-"*60)
    return helper


@calc_time
def fun(n):
    lst=[]
    for i in range(n):
        for j in range(i+1):
            lst.append(j**3)

fun(7000)


