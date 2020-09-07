import turtle 
exemplo = turtle.Turtle() 

"""_______________________________"""
"""    Movimento de tartaruga     """
""" ----------------------------- """

"""       Mover e desenhar        """
""" ----------------------------- """

exemplo.forward(75)         # Move para frente e desenha em pixels.
exemplo.fd(25)              # Move para frente e desenha em pixels.

exemplo.color("#FF0000")    # Troca de cor, cor em hexadecimal 

exemplo.backward(40)        # Move para trás e desenha em pixels.
exemplo.bk(10)              # Move para trás e desenha em pixels.
exemplo.back(5)             # Move para trás e desenha em pixels.

exemplo.color("green")      # Linha 9

exemplo.right(90)           # Vira para direita pelo angulo. 
# exemplo.rt()              # Vira para direita pelo angulo.  
exemplo.fd(25)              # Linha 7

exemplo.left(45)            # Vira para esquerda pelo angulo. 
# exemplo.lt()              # Vira para esquerda pelo angulo.

exemplo.color("#0000FF")    # Linha 9

exemplo.goto(10, 20)        # Move para posição x, y
# exemplo.setpos()          # Move para posição x, y
# exemplo.setposition()     # Move para posição x, y

exemplo.color("#7FFFD4")    # Linha 9

exemplo.setx(50)            # Move para posição x

exemplo.color("#006400")    # Linha 9
 
exemplo.sety(50)            # Move para posição y

exemplo.setheading(180)     # Aponta para angulo definido
# exemplo.seth()            # Aponta para angulo definido
# 0 = Direita
# 90 = Cima
# 180 = Esquerda
# 270 = Baixo
exemplo.color("#D2691E")    # Linha 9

exemplo.home()              # Volta para posição inicial 0,0

exemplo.color("#8A2BE2")    # Linha 9

exemplo.setheading(90)     # Linha 38

exemplo.circle(50, 180)    # Desenha circulo, 'graus, tamanho'

exemplo.color("#ADFF2F")   # Linha 9

exemplo.dot(10)            # Desenha um ponto

# print(exemplo.stamp())   # Retorna id da forma da turtle ??? FIXME
# exemplo.clearstamp()     # Apaga stamp FIXME
# exemplo.clearstamps()    # Apaga stmaps FIXME 

exemplo.dot(100)           # Linha 56

exemplo.undo()             # Desfaz a ultima ação

exemplo.speed(3)           # Define velocidade do desenho
# “fastest”: 0
# “fast”: 10
# “normal”: 6
# “slow”: 3
# “slowest”: 1

"""  Diga o estado da tartaruga   """
""" ----------------------------- """

print(exemplo.position())       # Retorna posição da tartaruga   
# exemplo.pos()

print(exemplo.towards(10, 1))   # Retorna angula da tartaruga pelo angulo passado

print(exemplo.xcor())           # Retorna coordenada de x
print(exemplo.ycor())           # Retorna coordenada de y

# exemplo.heading()
# exemplo.distance()


"""    Configuração e medição     """
""" ----------------------------- """

# exemplo.degrees()
# exemplo.radians()

"""_______________________________"""
"""      Controle de caneta       """
""" ----------------------------- """

"""       Estado de desenho       """
""" ----------------------------- """

# exemplo.pendown() | pd() | down()
# exemplo.penup() | pu() | up()
# exemplo.pensize() | width()
# exemplo.pen()
# exemplo.isdown()
# exemplo.Color control
# exemplo.pencolor()
# exemplo.fillcolor()
# exemplo.Filling
# exemplo.filling()
# exemplo.begin_fill()
# exemplo.end_fill()

""" ----------------------------- """
""" More drawing control """
""" ----------------------------- """

# exemplo.reset()
# exemplo.clear()
# exemplo.write()
# exemplo.Turtle state
# exemplo.Visibility
# exemplo.showturtle() | st()
# exemplo.hideturtle() | ht()
# exemplo.isvisible()
# exemplo.Appearance
# exemplo.shape()
# exemplo.resizemode()
# exemplo.shapesize() | turtlesize()
# exemplo.shearfactor()
# exemplo.settiltangle()
# exemplo.tiltangle()
# exemplo.tilt()
# exemplo.shapetransform()
# exemplo.get_shapepoly()
# exemplo.Using events
# exemplo.onclick()
# exemplo.onrelease()
# exemplo.ondrag()

""" ----------------------------- """
""" Special Turtle methods """
""" ----------------------------- """

# exemplo.begin_poly()
# exemplo.end_poly()
# exemplo.get_poly()
# exemplo.clone()
# exemplo.getturtle() | getpen()
# exemplo.getscreen()
# exemplo.setundobuffer()
# exemplo.undobufferentries()

""" ----------------------------- """
""" Methods of TurtleScreen/Screen """
""" Window control """
""" ----------------------------- """

# exemplo.bgcolor()
# exemplo.bgpic()
# exemplo.clear() | clearscreen()
# exemplo.reset() | resetscreen()
# exemplo.screensize()
# exemplo.setworldcoordinates()
# exemplo.Animation control
# exemplo.delay()
# exemplo.tracer()
# exemplo.update()
# exemplo.Using screen events
# exemplo.listen()
# exemplo.onkey() | onkeyrelease()
# exemplo.onkeypress()
# exemplo.onclick() | onscreenclick()
# exemplo.ontimer()
# exemplo.mainloop() | done()
# exemplo.Settings and special methods
# exemplo.mode()
# exemplo.colormode()
# exemplo.getcanvas()
# exemplo.getshapes()
# exemplo.register_shape() | addshape()
# exemplo.turtles()
# exemplo.window_height()
# exemplo.window_width()
# exemplo.Input methods
# exemplo.textinput()
# exemplo.numinput()
# exemplo.Methods specific to Screen
# exemplo.bye()
# exemplo.exitonclick()
# exemplo.setup()
# exemplo.title()

turtle.done()       # Inicia evento de loop 'trava tela'