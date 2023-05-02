cont = 0 #inicializando a variável para contar as idades
for valor in range(1,6):
    idade = int(input("Informe sua idade: "))

    if idade >= 18:
        cont = cont + 1

print(f"O total de pessoas com mais de 18 é {cont}")
