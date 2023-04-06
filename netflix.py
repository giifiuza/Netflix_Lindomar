class Cliente:
    def __init__(self, nome='', email='', plano='basic', tipo='user'): #metodo construtor
        self.nome = nome
        self.email = email
        self.planos = ['basic', 'medium', 'premium']
        if plano in self.planos:
            self.plano = plano
        else:
            print('Plano inválido.')
            self.plano = ''
        self.tipos = ['user', 'admin']
        if tipo in self.tipos:
            self.tipo = tipo
        else:
            print('Tipo de usuário inválido.')
            self.tipo = ''

    def mudar_plano(self, novoPlano):
        if novoPlano in self.planos:
            self.plano = novoPlano
        else:
            print('Plano inválido.')

    def ver_filme(self, filme, planoFilme):
        if self.plano == 'premium' or self.plano == planoFilme:
            print(f'o cliente {self.nome} pode assistir {filme}')
        elif self.plano == 'medium' and planoFilme =='basic':
            print(f'o cliente {self.nome} \33[31m pode \33[massistir {filme}')
        else:
            print(f'o cliente {self.nome} \33[31mNÃO pode \33[massistir {filme}')