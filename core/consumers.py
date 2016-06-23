import time


def hello(message):
    print('Hello 1 start ', time.ctime())
    time.sleep(5)
    print('Hello 1 end   ', time.ctime())

def hello2(message):
    print('Hello 2 start ', time.ctime())
    time.sleep(3)
    print('Hello 2 end   ', time.ctime())

def foo(message):
    print('foo start     ', time.ctime())
    time.sleep(4)
    print('foo end       ', time.ctime())
