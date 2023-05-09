lanche = ("pizza", "hotdog", "refri", "batata")
idades = tuple() # outra forma de criar tuplas

print(lanche)
print(type(lanche)) # estou mostrando o tipo da variável

print(lanche[1])
print(f" o total de lanches é {len(lanche)} \n") #length

#lanche[2] = "Suco"

for contador in range(0, 4):
    print(lanche[contador])

print("-"*30)
for item in lanche:
    print(item)

print("-"*30)
# enumerate serve para permitir acessar os índices da tupla. Já a variável indice, irá armazenar os valores do índice
for indice,elemento in enumerate(lanche):
    print(f"{indice} = {elemento}")

