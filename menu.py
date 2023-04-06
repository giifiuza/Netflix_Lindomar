from read import listar_filmes, listar_usuarios
from create import cadastrar_usuario, cadastrar_filmes
from update import atualizar
usuario = []
usuarios = []

planos = ['basic', 'medium', 'premium']
tipos = ['admin', 'user']


def menu():
    while True:
        print('---------------------\n'
              f'Usuário: \n'
              f'Tipo: \n'
              '[0] - Sair\n'
              '[1] - Cadastrar Usuário\n'
              '[2] - Cadastrar Filme\n'
              '[3] - Login\n'
              '[4] - Listar Filmes\n'
              '[5] - Atualização\n'
              '---------------------\n')
        opcao = int(input('Escolha a opção: '))
        if opcao == 0:
            break

        elif opcao == 1:

            cadastrar_usuario()
        elif opcao == 2:
            cadastrar_filmes()
        elif opcao == 3:
           ...
            # cliente = input('Nome: ')
            # for x in range(len(usuarios)):
            #     if cliente == usuarios[x][0]:
            #         escolhido.append(usuarios[1][0])
            #         escolhido.append(usuarios[1][1])
            #         escolhido.append(usuarios[1][2])
            #         escolhido.append(usuarios[1][3])
            #     else:
            #         print("Usuário não cadastrado")
            # print(escolhido)

        elif opcao == 4:
            print(listar_filmes())
        elif opcao == 5:
            atualizar()

