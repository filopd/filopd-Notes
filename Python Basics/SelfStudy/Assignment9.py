from threading import *

def EvenNumbersThread():
    i = 1
    while(i<10):
        print(current_thread().getName())
        if(i%2 == 0):
            print("Even No: ", i)
        i += 1

def OddNumbersThread():
    i = 1
    while(i<10):
        print(current_thread().getName())
        if(i%2 != 0):
            print("Odd No: ", i)
        i += 1

def MainAllNumberThred():
    i = 1
    while(i<10):
        print(current_thread().getName())
        print("Normal No: ", i)
        i += 1

t1 = Thread(target=EvenNumbersThread)
t2 = Thread(target=OddNumbersThread)
t1.start()
MainAllNumberThred()
t2.start()

