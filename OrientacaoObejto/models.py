# -*- coding: UTF-8 -*-

class Perfil():
    'Classe padrão para perfis de usuário'
    def __init__(self, nome, telefone, idade, empresa):
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
        self.empresa = empresa

    def toString(self):
        print 'Nome %s, Telefone: %s, Idade: %s, Empresa: %s' % (self.nome, self.telefone, self.idade, self.empresa)

