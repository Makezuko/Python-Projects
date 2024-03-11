def programa():
    try:
        diagonalMaior = float(input('Insira o valor da maior diagonal do paralelogramo em cm: '))
        while diagonalMaior <= 0:
            print('Erro! o valor inserido precisa ser positivo.')
            diagonalMaior = float(input('Insira o valor da maior diaginal do paralelogramo em cm: '))
        if diagonalMaior > 0:
            diagonalMenor = float(input('Insira o valor da menor diagonal do paralelogramo em cm: '))
        while diagonalMenor <= 0:
            print('Erro! o valor inserido precisa ser positivo.')
            diagonalMenor = float(input('Insira o valor da menor diagonal do paralelogramo em cm: '))
        if diagonalMenor > 0:
            area = (diagonalMenor * diagonalMaior)/2
            print('O valor da área de um paralelogramo de diametros {:.2f}cm e {:.2f}cm é de {:.2f}cm quadrados'.format(diagonalMenor, diagonalMaior, area))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico.')
        programa()
print('Bem-vindo ao programa de área de um paralelogramo')
programa()