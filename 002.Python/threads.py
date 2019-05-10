import threading as thr # Thread para multiplos processos
import time

def fun1(num):
    for i in range(0, num):
        print("fun1 - {}".format(i))
        time.sleep(1)

def fun2(num):
    for i in range(0, num):
        print("fun2 - {}".format(i))
        time.sleep(1)

thr.Thread(target=fun1, args=(10,)).start()
thr.Thread(target=fun2, args=(10,)).start()
