# While funcionando como loop contado 
contador = 1

while contador <= 5:
    print(contador) 
    contador = contador + 1

# While funcionando como loop condicional
"""
senha = ""
while senha != "123":
    senha = input("Informe sua senha: ")

print("Obrigado por usar o sistema\n")
"""
#While como se fosse o faça - enquanto
while True:
    senha = input("Informe sua senha: ")
    if senha == "123":
        break

print("Obrigado")

 



