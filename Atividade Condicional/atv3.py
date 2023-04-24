salario = float(input("Informe seu salário: "))

if salario < 600:
    novoSalario = (salario * 0.3) + salario
    print(f"Seu novo salario é {novoSalario}\n")
else:
    print(f"Você não tem direito pois ganha {salario}\n")