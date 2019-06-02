from no import No

class ListaSimples:
    
    def __init__(self):
        self.cabeca = No(None)

    def esta_vazia(self):
        return self.cabeca.get_proximo() == None
    
    def adicionar(self, novo_no):
        if(self.esta_vazia()):
            self.cabeca.set_proximo(novo_no)
        else:
            atual = self.cabeca

            while(atual.get_proximo()):
                atual = atual.get_proximo()
            
            atual.set_proximo(novo_no)

    def percorrer(self):
        atual = self.cabeca.get_proximo()

        while(atual):
            print(atual.get_elemento())
            atual = atual.get_proximo()