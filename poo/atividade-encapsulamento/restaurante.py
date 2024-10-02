class Servico:
    def __init__(self, pedido=0):
        self.__pedido = pedido
    
    def novoPedido(self):
        self.__pedido += 1

    def cancelarPedido(self):
        if self.__pedido == 0:
            print("Não existem pedidos para cancelar atualmente :)")
        else:
            self.__pedido -= 1
    
    def exibirPedido(self):
        print(f"O total de pedidos realizados até o momento é: {self.__pedido}")

    