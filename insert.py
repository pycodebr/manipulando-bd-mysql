import mysql.connector

# Conecta no Banco de Dados #
mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="pycodebr")

# Cria Query, executa SQL e salva resgistros no Banco de Dados #
mycursor = mydb.cursor()
sql = "INSERT INTO clientes (nome, idade, email) VALUES (%s, %s, %s)"
val = [
("Felipe", 23, "felipe@gmail.com"),
("Paulo", 30, "paulo@gmail.com"),
("Maria", 19, "maria@gmail.com")
]
mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "Registros Inseridos")