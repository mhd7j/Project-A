import time

def say_hello():
    time.sleep(5)
    print("Hello Mosiyo")
    return

say_hello()

@say_hello
def funk():
    return
funk()