# -*- coding: UTF-8 -*-
# garante que o interpretador python processará sempre o arquivo usando a cadeia de caracter UTF-8
def cadastrar (nomes):
    print 'Digite o nome que deseja adicionar'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Digite o nome que deseja remover'
    nome_remover = raw_input()
    nomes.remove(nome_remover)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def alterar(nomes):
    print 'Digite o nome que deseja alterar'
    nome_alterar = raw_input()

    if(nome_alterar in nomes):
        print 'Digite o nome'
        
def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        # Para a entrada de dados se usa raw_input, onde irá travar o console até a entrada do dado
        print 'Digite 1- cadastrar,2-remover,3-Listar 4-Alterar 0-finalizar'
        escolha = raw_input()

        if (escolha == '1'): 
                cadastrar(nomes)

        if(escolha == '2'):
                remover(nomes)

        if(escolha == '3'):
            listar(nomes)

        if(escolha == '4'):
            alterar(nomes)

        else: 
            print 'Opção inválida, favor digitar um opção valida'

menu()
# Para compilar só digitar no console do from app import * depois selecionar a função

                
