import mysql.connector
from conectar import conexao, cursor
def atualizar():
    sql = ''
    while True:
        print('---------------------\n'
              'O que deseja atualizar\n'
              '[0] - Filmes\n'
              '[1] - Usuários\n'
              '---------------------\n')
        opcao = int(input('Escolha a opção: '))
        if opcao == 0:
            op = int(input('---------------------\n'
                  'O que deseja atualizar na tabela filmes?\n'
                  '[0] - Nome\n'
                  '[1] - Plano\n'
                  '[2] - Descrição\n'
                  '[3] - Classificação\n'))
            if op == 0:
                nome = input("Digite o nome novo: ")
                id = int(input("ID do filme que será atualizado: "))
                sql = f'UPDATE Filmes SET filme = "{nome}" WHERE id = "{id}" '
            elif op == 1:
                plano = input("Digite o plano novo: ")
                id = input("ID do filme que será atualizado: ")
                sql = f'UPDATE Filmes SET planoFilme = "{plano}" WHERE id = "{id}"'
            elif op == 2:
                descr = input("Digite a nova descrição: ")
                id = input("ID do filme que será atualizado: ")
                sql = f'UPDATE Filmes SET descricao = "{descr}" WHERE id = "{id}" '
            elif op == 3:
                classificacao = input("Digite a nova classificação: ")
                id = input("ID do filme que será atualizado: ")
                sql = f'UPDATE Filmes SET class = "{classificacao}" WHERE id = "{id}" '

        elif opcao == 1:
            opc = input('---------------------\n'
                       'O que deseja atualizar na tabela usuários?\n'
                       '[0] - Nome\n'
                       '[1] - Email\n'
                       '[2] - Plano\n')


        cursor.execute(sql)
        conexao.commit()  # edita o banco de dados


cursor.close()
conexao.close()

