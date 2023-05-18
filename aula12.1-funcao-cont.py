# FUNÇÃO COM RETORNO

nome = input("Informe seu nome: ")

def contarLetras(texto):
    #print(f" O nome possui o total de {len(texto)} letras")
    return len(texto)

print(contarLetras(nome))
