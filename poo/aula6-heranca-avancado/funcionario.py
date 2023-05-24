class Funcionario:
    def __init__(self,cargo,nome):
        self._cargo = cargo # Atributos estão com apenas 1 underline, protegidos
        self._nome = nome
    
    def informacoes(self):
        print(f"Olá {self._nome} seu cargo atual é {self._cargo}\n")

class Gerente(Funcionario):
    def __init__(self, cargo, nome, salario):
        super().__init__(cargo, nome) # super() significa que estamos usando a superclasse que é a classe mãe
        self._salario = salario
    
    def exibirSalario(self):
        print(f"Seu nome é {self._nome} e você ganha {self._salario}\n")
