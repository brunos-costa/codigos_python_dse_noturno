somaTurma = 0
somaMulheres = 0
contMulheres = 0
for contador in range(1,7):
    altura = float(input("Informe sua altura: "))
    sexo = int(input("Informe o código do sexo: 1-masc ou 2-fem: "))

    if contador == 1:
        menor = altura
        maior = altura
    else:
        if altura >= maior:
            maior = altura

        if altura <= menor:
            menor = altura
        
    if sexo == 2:
        somaMulheres += altura
        contMulheres += 1

    somaTurma += altura

print(f"A maior altura é {maior} e a menor altura é {menor}")
print(f"A média de alturas das mulheres é {somaMulheres / contMulheres}")
print(f"A média de alturas da turma é {somaTurma / 6}\n")