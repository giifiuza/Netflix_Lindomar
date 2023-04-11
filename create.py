# from conectar import conexao, cursor
from prettytable import PrettyTable

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='Netflix',
    user='root',
    password=''
)


cursor = conexao.cursor()

def cadastrar_filmes():
    filme = input('Digite o filme que queira cadastrar: ')
    planoFilme = input('Digite o plano do filme: ')
    descr = input('Digite a descrição do filme: ')
    idade = input('Digite a idade permitida: ')
    inserir_filmes = f'INSERT INTO Filmes (filme, planoFilme, descricao, class) values ("{filme}", "{planoFilme}", "{descr}", "{idade}")'

    cursor.execute(inserir_filmes)
    conexao.commit()

    sql = 'select * from Filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tab = PrettyTable()
    tab.field_names = ["Filme", "ID", "Plano", "Descrição", "Classificação"]

    for linha in linhas:
        tab.add_row(linha)
    print(tab)


def cadastrar_usuario(usuario, email, plano, tipo, idade):
    cadastro = f"""INSERT INTO Usuarios(nome, email, plano, tipo, idade)
     values
     ('{usuario}', '{email}', '{plano}', '{tipo}', {idade})"""
    cursor.execute(cadastro)
    conexao.commit()

    sql = 'select * from Usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall() #fetchall coloca dentro de uma lista
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)


# def login(usuarios):
#     usuario = input('Digite nome de usuario: ')
#     if usuario in usuarios:














