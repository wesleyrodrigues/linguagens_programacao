class No:
    def __init__(self, novo_elemento):
        self.elemento = novo_elemento
        self.proximo = None
    
    def get_elemento(self):
        return self.elemento
    
    def get_proximo(self):
        return self.proximo

    def set_elemento(self, novo_elemento):
        self.elemento = novo_elemento

    def set_proximo(self, proximo_elemento):
        self.proximo = proximo_elemento
    
