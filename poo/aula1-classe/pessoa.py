class Pessoa:
    # atributos
    nome = "Fulano"
    idade = 30
    altura = 1.65

    # métodos
    def falar(self, texto):# self é um parâmetro obrigatório do python que informa que o método pertence à própria classe que foi criada
        print(texto)

pessoa1 = Pessoa()
pessoa1.nome = "José"
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar("Olá mundo")