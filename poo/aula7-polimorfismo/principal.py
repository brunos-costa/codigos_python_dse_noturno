from produto import Produto, Livro, Eletronico

meuLivro = Livro("Hoje é quinta", 56, "Fulano Cury")
meuEletro = Eletronico("Smartphone", 2000, "Pirafone")

meuLivro.descrever()
meuLivro.calcularPreco()

meuEletro.calcularPreco()