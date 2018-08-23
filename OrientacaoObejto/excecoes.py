# -*- coding: UTF-8 -*-
from models import *
perfis = Perfil.gerar_perfis('teste.csv')
# try:
#     arq = open('inexistente.csv','r')
#     arq.close()
#     print('Arquivo lido')
# # posso passar varios tipos de erro para um mesmo tratamento
# except (IOError, TypeError) as erro:
#     print('Erro tratado %s' % erro)