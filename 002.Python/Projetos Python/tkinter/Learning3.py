# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
from tkinter import RIGHT, Button, Frame, Label, Tk


class Learning3:
    def __init__(self, master=None):  # .
        self.widget1 = Frame(master)  # .!frame
        # self.widget1.pack() # version 1.0
        self.widget1.pack(side=RIGHT)  # version 2.0 learning.txt L12
        # .!frame.!label
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        # self.msg.pack() # version 1.0
        self.msg.pack(side=RIGHT)  # version 2.0
        self.sair = Button(self.widget1)  # .!frame.!button
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["command"] = self.widget1.quit
        # self.sair.pack() # version 1.0
        self.sair.pack(side=RIGHT)  # version 2.0


root = Tk()
Learning3(root)
root.mainloop()
