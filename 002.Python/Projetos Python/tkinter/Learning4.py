# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
from tkinter import Button, Frame, Label, Tk

# event handlers learning.txt L14


class Learning4:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack()
        self.button = Button(self.widget1)
        self.button["text"] = "Clique aqui"
        self.button["font"] = ("Calibri", "9")
        self.button["width"] = 10  # learning.txt L6
        # self.button.bind("<Button-1>", self.mudarTexto) # version 1.0 learning.txt L15
        self.button["command"] = self.mudarTexto  # version 2.0
        self.button.pack()

    # def mudarTexto(self, event): # version 1.0
    def mudarTexto(self):  # version 2.0
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Learning4(root)
root.mainloop()
