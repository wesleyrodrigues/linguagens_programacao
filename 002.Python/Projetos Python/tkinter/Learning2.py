# https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
# Testando primeiro widget
from tkinter import Frame, Label, Tk


class Learning2:
    def __init__(self, master=None):
        self.widget1 = Frame(master) # O frame master é a janela principal
        self.widget1.pack() # widget1 container
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack() # geometria e posicionamento


root = Tk()
Learning2(root)
root.mainloop()  # mantem o app em execução
