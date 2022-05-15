import time

def def_1(func):
    def def_2():
        func()
        print(time.perf_counter())
    return def_2

@def_1
def def_3():
    print("it took time Mosiyo :")






def_3()