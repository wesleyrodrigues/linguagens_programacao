import turtle
# import threading as thr  # Thread para multiplos processos
from threading import Thread
from random import randint
import time

def color(): return randint(0, 255)

class Th(Thread):
    def __init__ (self, turtleArg, pos):
        Thread.__init__(self)
        self.turtleArg = turtleArg
        self.pos = pos
    
    def run(self):
        self.turtleArg.shape("turtle")
        self.turtleArg.pensize(5)
        self.turtleArg.color('#%02X%02X%02X' % (color(), color(), color()))
        self.turtleArg.speed(0)
        self.turtleArg.goto(-500+self.pos, -300+self.pos)
        # turtleArg.setx(pos)
        self.turtleArg.clear()
        for i in range(0, 4):
            self.turtleArg.forward(self.pos)
            self.turtleArg.right(90)
        
        self.turtleArg.ht()

# def teste1():
time.sleep(5)
for i in range(0, 80, 2):
    Th(turtle.Turtle(), i*5).start()

    # t = thr.Thread(target=square, args=(turtle.Turtle(), i*5.))
    # t.isAlive()
    # t.start()
    # t.join()

screen = turtle.Screen()
screen.mainloop()


# turtle.done()