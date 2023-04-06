from conectar import conexao, cursor
from prettytable import PrettyTable


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


def cadastrar_usuario():
    usuarios = []
    usuario = input('Digite nome de usuario: ')
    email = input("Digite o email: ")
    print("Plano: basic | medium | premium |")
    plano = input("Digite o plano: ")
    print("Admin | User")
    tipo = input("Tipo de conta: ")
    idade = input("Digite sua idade: ")

    cadastro = f"""INSERT INTO Usuarios(nome, email, plano, tipo, idade)
     values
     ('{usuario}', '{email}', '{plano}', '{tipo}', {idade})"""

    usuarios.append(usuario)
    cursor.execute(cadastro)
    conexao.commit()
    return usuarios


# def login(usuarios):
#     usuario = input('Digite nome de usuario: ')
#     if usuario in usuarios:












