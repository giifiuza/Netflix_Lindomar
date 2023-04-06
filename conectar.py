import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='Netflix',
    user='root',
    password=''
)


cursor = conexao.cursor()
