def programa():
    try:
        lados = int(input('Insira a quantidade de lados que o polígono regular possui: '))
        if lados <= 0:
            print('Erro! Você precisa inserir um valor positivo.')
            programa()
        if lados > 0:
            valor_lados = float(input('Insira o valor de um dos lados do polígono em cm: '))
            while valor_lados <= 0:
                print('Erro! Você precisa inserir um valor positivo')
                valor_lados = float(input('Insira o valor de um dos lados do polígono em cm: '))
            perimetro = lados * valor_lados
            print('O valor do perímetro de um polígono regular de {} lados de {:.2f}cm é de {:.2f}cm'.format(lados, valor_lados, perimetro))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico')
        programa()
print('Bem-vindo/a à calculadora de perímetros de polígonos regulares.')
programa()