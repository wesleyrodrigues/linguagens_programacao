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

# from threading import Thread

#        class Th(Thread):

#                 def __init__ (self, num):
#                       Thread.__init__(self)
#                       self.num = num

#                 def run(self):

#                       print "Hello "
#                       print self.num


#        a = Th(1)
#        a.start() 