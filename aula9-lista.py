notas = [9.5, 7.0, 6.5, 9]
print(notas)
print(type(notas))

for item in notas:
    print(item)

notas[2] = 8.5

print("="*30)
print(notas)

# Inserindo valores na lista
# Forma 1
notas.append(4)# vai inserir o item no final da lista
print(notas, "\n")

#Forma 2
notas.insert(1,10)# insert precisa de 2 parâmetro. 1- é o índice que desejo inserir o valor. 2- é o valor propriamente dito que quero inserir
print(notas, "\n")

#Removendo valores
#Forma 1
notas.pop()# exclui o último elemento
print(notas, "\n")

#Forma 2
notas.pop(2) # removendo pelo indice
print(notas,"\n")

#Forma 3
notas.remove(9.5)# o remove() exclui usando o conteúdo da lista como parâmetro
print(notas,"\n")