def soletrar():
    print 'Digite a frase que deseja soletrar'
    frase = raw_input()
    contador = 0
    while (contador< len(frase)):
        print frase[contador]
        contador+=1
    print 'FIM'