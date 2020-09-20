import turtle
import threading as thr  # Thread para multiplos processos
from random import randint


from datetime import datetime
# window = turtle.Screen()
# window.bgcolor("black")

def color(): return randint(0, 255)
def aNumber(): return randint(2, 200)
def graus(): return randint(-360, 360)
# def gotoX(): return randint(-669, 669)
# def gotoY(): return randint(-339, 339)

def aleatorio(al):
    al.speed(0)
    al.pensize(5)
    al.shape("turtle")
    for i in range(0, 3):
        al.color('#%02X%02X%02X' % (color(), color(), color()))
        print(al, end="")
        print(f' {i}')
        # al.goto(gotoX(), gotoY())
        al.right(graus())
        al.forward(200)
        loc = al.position()
        # if(i == 1):
        #     al.clear()
        if(loc[0] > 670
           or loc[0] < -670
           or loc[1] > 340
           or loc[1] < -340):
        #    al.goto(0, 0)
            break

for i in range(0, 50):
    thr.Thread(target=aleatorio, args=(turtle.Turtle(),)).start()

turtle.done()
