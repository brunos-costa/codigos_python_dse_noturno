class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def descrever(self):
        print(f"O produto possui o preço R$ {self._preco}")
    
    def calcularPreco(self):
        pass

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self._autor = autor

    def descrever(self):
        print(f"Livro: {self._nome} - Autor: {self._autor}\n")
    
    def calcularPreco(self):
        print(f"O livro custa R${self._preco}")

class Eletronico(Produto):
    def __init__(self, nome, preco, marca):
        super().__init__(nome, preco)
        self._marca = marca

    def calcularPreco(self):
        print(f"O eletrônico, da marca {self._marca} custará o valor de R$ {self._preco * 1.2}")