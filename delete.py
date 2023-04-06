import mysql.connector
from conectar import conexao, cursor


deleta = f'DELETE FROM Filmes WHERE filme = "Titanic"'
cursor.execute(deleta)
conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()