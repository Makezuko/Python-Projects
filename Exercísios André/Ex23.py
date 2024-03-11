def programa():
    try:
        baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
        basem = float(input('Insira o valor da menor base do trapézio en cm: '))
        while baseM <= 0 or basem <= 0:
            print('Erro! O valor inserido deve ser positivo.')
            baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
            basem = float(input('Insira o valor da menor base do trapézio en cm: '))
        while baseM < basem:
            print('Erro! A base maior tem que ser maior que a base menor.')
            baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
            basem = float(input('Insira o valor da menor base do trapézio en cm: '))
        if baseM > basem:
            altura = float(input('Insira o valor da altura do trapézio em cm: '))
            while altura <= 0:
                print('Erro! O valor inserido deve ser positivo.')
                altura = float(input('Insira o valor da altura do trapézio em cm: '))
            if altura > 0:
                area = ((baseM + basem)*altura)/2
                print('O valor da área de um trapézio de bases {:.2f}cm e {:.2f}cm, com {:.2f}cm de altura é de {:.2f}cm quadrados'.format(baseM, basem, altura, area))
    except ValueError:
        print('Erro! Os valores solicitados devem ser numéricos.')
        programa()
print('Bem-vindo ao programa de cálculo de área de um trapézio')
programa()