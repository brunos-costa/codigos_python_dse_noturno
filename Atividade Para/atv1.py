soma = 0
media = 0
total = 0

for contador in range(50, 70):
    total = total + 1
    soma = soma + contador # acumulando os valores
    media = soma / total

print(f"O total é {total}\n a soma é {soma}\n e a média é {media}\n")
