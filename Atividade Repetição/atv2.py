contador = 1
totalHotel = 0
somaHotel = 0

while contador <= 8:
    nome = input("Informe seu nome: ")
    dias = int(input("Quantos dias você ficou no hotel? "))

    totalDiarias = dias * 50 
    if dias < 15:
        taxa = dias * 4  

    elif dias == 15:
        taxa = dias * 3.60  
    
    elif dias > 15:
        taxa = dias * 3     
    
    totalHotel = totalDiarias + taxa # O valor que o hotel vai receber
    print(f"Olá {nome} você ficou {dias} dias e vai pagar R${totalDiarias + taxa}")
    somaHotel +=totalHotel

print(f"O hotel irá receber um total de R${somaHotel}")