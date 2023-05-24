class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def relatorio(self):
        print(f"Olá {self.__titular} o número da sua conta é {self.__numero} e o seu saldo atual é R${self.__saldo} e o seu limite é R$ {self.__limite}")
        
    def exibirSaldo(self):
        print(f"Seu saldo é {self.__saldo}")

    # O método get irá retornar ou exibir o valor do atributo
    def getLimite(self):
        return self.__limite
    
    # O método set irá alterar o conteúdo do atributo, sem exibir nada 
    def setLimite(self, valor):
        if valor < 0:
            print("Valor menor que zero, informe outro valor")
        else:
            self.__limite = valor

    # VAMOS MODIFICAR O ATRIBUTO SALDO COM @PROPERTY E @SETTER
    @property
    def saldo(self):
        print(f"Olá, seu saldo é {self.__saldo}\n")
    
    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print("Você não pode inserir valor negativo ou zero\n")
        else:
            self.__saldo = valor