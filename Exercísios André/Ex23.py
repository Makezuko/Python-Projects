def programa():
    try:
        baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
        basem = float(input('Insira o valor da menor base do trapézio en cm: '))
        while baseM < basem:
            print('Erro! A base maior tem que ser maior que a base menor.')
            baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
            basem = float(input('Insira o valor da menor base do trapézio en cm: '))
        if baseM > basem:
            altura = float(input('Insira o valor da altura do trapézio em cm: '))
    except ValueError:
        print('Erro! Os valores solicitados devem ser numéricos.')
        programa()