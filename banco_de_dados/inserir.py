import pymysql

#Estabelecendo a conexão
conexao = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="departamento_bd"
)

#Inserindo dados no banco
codigo = int(input("Informe o código do funcionário: "))
nome = input("Informe o nome do funcionário: ")
salario = float(input("Informe o salário do funcionário: "))
cargo = input("Informe o cargo do funcionário: ")

# colocamos %s no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca pymysql
comando = "insert into funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo)# Criando um tupla com os dados que serão substituídos no comando

consulta = conexao.cursor()# cursor() é o objeto que irá interagir diretamente com o banco de dados

consulta.execute(comando, campos)

conexao.commit()# gravar os dados no banco

print(consulta.rowcount, " linha(s) inserida com sucesso\n")

conexao.close()