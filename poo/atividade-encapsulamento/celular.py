class Celular:
    def __init__(self, numero, saldo=0, plano="pré-pago", valorMinuto = 1.5):
        self.__numero = numero
        self.__saldo = saldo
        self.__plano = plano
        self.__valorMinuto = valorMinuto

    @property
    def plano(self, novoPlano):
        return self.__plano
    
    @plano.setter
    def plano(self, novoPlano):
        self.__plano = novoPlano

    def recarregar(self, valor):
        if self.__plano == "pré-pago":
            if valor <= 0:
                print("Informe um valor de recarga válido")
            else:
                self.__saldo += valor
        else:
            print(f"O seu plano é pós-pago, não precisa recarregar! ")
    
    def fazerChamada(self, duracao):
        custoTotalChamada = duracao * 1.5 #custo total da chamada
        if self.__plano == "pré-pago":
            if self.__saldo <= 0 or custoTotalChamada > self.__saldo:
                print("Saldo insuficiente para fazer chamada")
            else:
                self.__saldo -= custoTotalChamada
                print(f"Você fez uma chamada de {duracao} minutos e gastou um total de R$ {custoTotalChamada}, assim seu saldo atual é de {self.__saldo}")
        else:
            print(f"O valor de R${custoTotalChamada} será cobrado na fatura no final do mês")
    def exibirDados(self):
        print(f"Seu número atual é {self.__numero}")
        print(f"Seu saldo atual é R${self.__saldo}")
        print(f"Seu plano atual é {self.__plano}")
        