class Conta:
    # Construtor, irá iniciar automaticamente.
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero  # Atributo
        self.__titular = titular  # __ = privado (private)
        self.__saldo = saldo
        self.__limite = limite

    # def get_titular(self):
    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):  # conta.saldo
        return self.__saldo

    @property  # conta.limite
    def limite(self):  # Melhora a legibilidade
        return self.__limite

    @limite.setter  # conta.limite = 200.00
    def limite(self, limite):  # Melhora a legibilidade
        self.__limite = limite

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def deposita(self, valor):
        self.__saldo += valor

    def extrato(self):
        print("Titular {} valor em conta {}".format(
            self.__titular, self.__saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @staticmethod
    def codigo_banco():  # Método estático. # Pode ser acessado diretamente Conta.codigo_banco()
        return "001"

conta = Conta(4568, "Wesley", 200.00, 1000.00)
conta1 = Conta(4578, "William", 500.00, 3000.00)

print(conta.titular) # Wesley
print(conta.saldo) # 200.00
print(conta.limite) # 1000.00

conta.saca(1300.00) # O valor 1300.0 passou o limite
conta.saca(300)

print(conta.saldo) # -100.0
print(conta.limite) # 1000.0

conta.deposita(200)
conta.extrato() # Titular Wesley valor em conta 100.0
conta1.transfere(100, conta)
conta.extrato() # Titular Wesley valor em conta 200.0

print(conta.codigo_banco()) # 001
