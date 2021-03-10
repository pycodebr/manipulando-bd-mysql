import mysql.connector

# Conecta no Banco de Dados #
mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="pycodebr")

# Cria Query, executa SQL e captura os dados retornados #
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM clientes")
clientes = mycursor.fetchall()

# Mostra registros #
for cliente in clientes:
    print(cliente)