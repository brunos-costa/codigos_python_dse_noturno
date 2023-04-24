salario = float(input("Informe seu salário: "))
financiamento = float(input("Qual o valor do financiamento: "))

valor5x = financiamento * 5

if valor5x <= salario:
    print("Financiamento concedido\n")
else:
    print("Financiamento não concedido\n")

print("Obrigado por nos consultar\n")