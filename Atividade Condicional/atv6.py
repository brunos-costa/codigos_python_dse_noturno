percurso = float(input("Informe o percurso em km: "))
tipoCarro = int(input("Informe o tipo do carro, 1, 2 ou 3: "))

if tipoCarro == 1:
    total = percurso / 8
    #print(f"o tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina\n")

elif tipoCarro == 2:
    total = percurso / 9
    #print(f"o tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina\n")

elif tipoCarro == 3:
    total = percurso / 12
    #print(f"o tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina\n")



print(f"o tipo do carro é {tipoCarro} vai precisar de {total} litros de gasolina\n")