import turtle
# import threading as thr  # Thread para multiplos processos
# from threading import Thread
from random import randint
import time

def color(): return randint(0, 255)
    
def run(turtleArg, col, linha):
    turtleArg.shape("turtle")
    turtleArg.pensize(2)
    turtleArg.color('#%02X%02X%02X' % (color(), color(), color()))
    turtleArg.speed(0)
    turtleArg.goto(col, linha)
    # turtleArg.setx(pos)
    # turtleArg.clear()
        # for i in range(0, 4):
        #     turtleArg.forward(pos)
        #     turtleArg.right(90)
        
        # turtleArg.ht()

# def teste1():
# time.sleep(5)
tamc = 34
taml = 17
esp = 20

for c in range(0, tamc):
    for l in range(0, taml):
        if(c >= l):
            # Th(turtle.Turtle(), c*esp, l*esp).start()
            run(turtle.Turtle(), -660+c*esp*2, -320+l*esp*2)

    # t = thr.Thread(target=square, args=(turtle.Turtle(), i*5.))
    # t.isAlive()
    # t.start()
    # t.join()

screen = turtle.Screen()
screen.mainloop()


# turtle.done()