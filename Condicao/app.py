# -*- coding: UTF-8 -*-
# garante que o interpretador python processará sempre o arquivo usando a cadeia de caracter UTF-8
import re

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
# para percorrer o vetor e se encontrar o nome cai dentro da condicao
    if(nome_alterar in nomes):
        posicao = nomes.index(nome_alterar)
        print 'Digite o novo nome'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo

def buscar(nomes):
    print 'Digite o nome que deseja buscar'
    nome_buscar = raw_input()

    if(nome_buscar in nomes):
        print 'Nome %s  foi achado com sucesso na pos ' % (nome_buscar)
    else:
        print 'Nome %s  não foi achado com sucesso na pos ' % (nome_buscar)

def regex(nomes):
    print 'Digite a expressão regular'
    regex = raw_input()
    concatenado = ' '.join(nomes)
    busca = re.findall(regex, concatenado)
    print (busca)

        
def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        # Para a entrada de dados se usa raw_input, onde irá travar o console até a entrada do dado
        print 'Digite 1- cadastrar,2-remover,3-Listar, 4-Alterar, 5-Buscar, 6-Regex 0-finalizar'
        escolha = raw_input()

        if(escolha == '1'): 
                cadastrar(nomes)

        if(escolha == '2'):
                remover(nomes)

        if(escolha == '3'):
            listar(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            buscar(nomes)
        if(escolha == '6'):
            regex(nomes)


menu()
# Para compilar só digitar no console do from app import * depois selecionar a função

                
