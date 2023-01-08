from tkinter import *
from PIL import ImageTk, Image


class Forca:
    def __init__(self, master=None):
        self.cont = 1
        self.img = ImageTk.PhotoImage(Image.open(f"forca1.png"))
        self.fontePadrao = ("Arial", "30")
        self.palavra_d = ""

        self.palavra_program = ""

        self.imagemContainer = Frame(master)
        self.imagemContainer["pady"] = 10
        self.imagemContainer.pack()

        self.palavraContainer = Frame(master)
        self.palavraContainer["padx"] = 20
        self.palavraContainer["pady"] = 5
        # self.palavraContainer["bg"] = self.corPadrao
        self.palavraContainer.pack_forget()

        self.inputTextContainer = Frame(master)
        self.inputTextContainer["padx"] = 20
        self.inputTextContainer["pady"] = 5
        # self.inputTextContainer["bg"] = self.corPadrao
        self.inputTextContainer.pack()

        self.imageLabel = Label(self.imagemContainer, image=self.img)
        # self.imageLabel["bg"] = self.corPadrao
        self.imageLabel.pack(side=TOP)

        self.qtdLetrasLabel = Label(self.imagemContainer)
        self.qtdLetrasLabel.pack(side=BOTTOM)
        self.qtdLetrasLabel["font"] = self.fontePadrao
        self.qtdLetrasLabel.pack_forget()

        self.palavraLabel = Label(self.imagemContainer, font=self.fontePadrao)
        # self.palavraLabel["bg"] = self.corPadrao
        self.palavraLabel.pack_forget()
        # self.palavraLabel.pack(side=BOTTOM)

        self.pLabel = Label(self.imagemContainer, font=self.fontePadrao)
        self.pLabel["fg"] = "red"
        self.pLabel["height"] = 2
        self.pLabel.pack_forget()
        # self.pLabel.pack(side=TOP)

        self.letra = Entry(self.inputTextContainer)
        self.letra["width"] = 3
        self.letra["font"] = self.fontePadrao
        self.letra.bind("<Return>", self.palavra)
        # self.letra.bind("<Button-3>", self.palavra)
        self.letra.pack_forget()
        # self.letra.pack(side=TOP)

        self.palavra_certa = Entry(self.inputTextContainer)
        self.palavra_certa["width"] = 25
        self.palavra_certa["font"] = self.fontePadrao
        self.palavra_certa.bind("<Return>", self.iniciar)
        self.palavra_certa.pack(side=BOTTOM)

    def iniciar(self, event):
        self.palavra_certa.pack(side=BOTTOM)
        self.palavra_certa.pack_forget()
        self.palavraContainer.pack()
        self.inputTextContainer.pack()
        self.imageLabel.pack(side=TOP)
        self.qtdLetrasLabel.pack(side=TOP)
        self.palavraLabel.pack(side=BOTTOM)
        self.pLabel.pack(side=TOP)
        self.letra.pack(side=BOTTOM)

        palavra_certa = self.palavra_certa.get().upper()
        self.palavra_d = palavra_certa
        self.palavra_program = "_" * len(palavra_certa)
        self.qtdLetrasLabel["text"] = f"{len(self.palavra_d)} letras"
        self.palavraLabel["text"] = "".join(
            ["_ " if i != " " else "  " for i in self.palavra_d])
        self.pLabel["text"] = "" * len(self.palavra_d)

    def show_palavra(self):
        palavra_com_espaco = ""
        for i in self.palavra_program:
            palavra_com_espaco += i + " "
        return palavra_com_espaco

    def palavra(self, event):
        l = self.letra.get().upper()

        p = [i for i in self.palavra_program]

        if (l in self.palavra_d):
            for i in range(0, len(self.palavra_d)):
                if (self.palavra_d[i] == l):
                    p[i] = l
                elif (self.palavra_d[i] == " "):
                    p[i] = " "
            self.palavra_program = "".join(p)
            self.palavraLabel["text"] = self.show_palavra()

            if (not ("_" in self.palavra_program)):
                labelImage = ImageTk.PhotoImage(Image.open(f"ganhou.png"))
                self.imageLabel.configure(image=labelImage)
                self.imageLabel.image = labelImage
        elif (l in self.pLabel["text"]):
            pass
        else:
            self.cont = self.cont + 1
            self.pLabel["text"] += l + " "
            labelImage = ImageTk.PhotoImage(
                Image.open(f"forca{min(self.cont, 7)}.png"))
            self.imageLabel.configure(image=labelImage)
            self.imageLabel.image = labelImage

            if self.cont > 6:
                self.palavraLabel["text"] = self.palavra_d

        self.letra.delete(0, "end")


root = Tk()
root.title("Forca")
forca = Forca(root)
# root.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/icon.ico")
root.mainloop()
