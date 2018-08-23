# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuário'
    def __init__(self, nome, telefone, idade, empresa):
        if (len(nome)< 3):
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        self.nome = nome
        self.telefone = telefone
        self.idade = idade
        self.empresa = empresa
        self.__curtidas = 0
        self.armazenar_perfis(self.nome, self.idade, self.empresa)

    def toString(self):
        print 'Nome %s, Telefone: %s, Idade: %s, Empresa: %s' % (self.nome, self.telefone, self.idade, self.empresa)

    def curtir (self):
        # deixar a variavel encapsulada, pois no python não existe a função private
        # o python com esse underline, ele gera um nome aleatorio para a variavel não permitindo assim quando nós chamarmos, o acesso a ela
        self.__curtidas+=1
    
    def obter_curtidas(self):
        return self.__curtidas

        # para acessar esse metodo não precisamos ter que criar um novo perfil, basta apenas chamar o nome da classe, funcionando como um metodo de classe
    @staticmethod
    def gerar_perfis(nome_arq):
        arq = open(nome_arq, 'r')
        perfis = []
        for linha in arq:
            valores = linha.split(',')
            perfis.append(Perfil(*valores))
        arq.close()
        return perfis
    
    def armazenar_perfis(self, nome, idade,empresa):
        linhas = "%s , %s, %s \n" % (self.nome, self.idade, self.empresa)
        arq = open('armazenado.txt', 'a')
        arq.write(linhas)
        arq.close()
        return 'Armazenado'

# declaro que ela herda caracteristicas da classe
class Perfil_Vip(Perfil):
    'Classe para perfis VIP dos usuários'
    def __init__(self, nome, telefone, idade, empresa, apelido):
    # passar os meus dados que eu receber da classe filha para o construtor da classe pai
        super(Perfil_Vip, self).__init__(nome, telefone, idade,empresa)
        self.apelido = apelido

    def obter_creditos(self):
        # vai passar como parametro a classe filha e o self da classe filha para que possamos usar os valores da classe pai
        # como o atributo curtidas é privado precisamos passar o metodo que nos retorne o valor delas
        return super(Perfil_Vip, self).obter_curtidas() *10.0