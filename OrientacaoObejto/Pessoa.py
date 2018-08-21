# -*- coding: UTF-8 -*-

class Pessoa():
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)
    
    def calcularIMC(self):
        IMC = self.peso / (self.altura * self.altura)
        print 'IMC do %s é: %s' % (self.nome, IMC)