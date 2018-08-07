def gera_nome(convite):
    # pega o tamanho da string
    pos_final = len(convite) 
    pos_inicial = pos_final - 4
    part1 = convite[0:4]
    part2 = convite[pos_inicial: pos_final]
#     # print '%s %s' % (part1, part2)
    return part1 + ' ' + part2

def envia_conv(nome):
    return 'Enviando convite para ' + nome

def processa_convite(convite):
    nome = gera_nome(convite)
    return envia_conv(nome)
    
    



