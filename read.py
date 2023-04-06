import mysql.connector
from prettytable import PrettyTable
from conectar import conexao, cursor

def listar_usuarios():
    sql = 'select * from Usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall() #fetchall coloca dentro de uma lista
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)

def listar_filmes():
    sql = 'select * from Filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tab = PrettyTable()
    tab.field_names = ["Filme", "ID", "Plano", "Descrição", "Classificação"]

    for linha in linhas:
        tab.add_row(linha)
    print(tab)
