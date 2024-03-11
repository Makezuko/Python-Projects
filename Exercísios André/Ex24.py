def programa():
    try:
        quantidadeLados = int(input('Insira a quantidade de lados do polígono regular: '))
        base = float(input('Insira o valor da base em cm: '))
        apotema = float(input('Insira o valor da apótema em cm: '))
        while quantidadeLados < 3:
            print('Erro! A quantidade de lados de um polígono deve ser maior ou igual a 3.')
            programa()
        while quantidadeLados <= 0 or base <= 0 or apotema <= 0:
            print('Erro! Os valores precisam ser positivos.')
            programa()
        if quantidadeLados > 0 and base > 0 and apotema > 0:
            area = (quantidadeLados * base * apotema)/2
            print('A área de um polígono de {} lados, com base {:.2f}cm e apótema {:.2f}cm, é de {:.2f}cm quadrados.'.format(quantidadeLados, base, apotema, area))
    except ValueError:
        print('Erro! Você precisa inserir valores numéricos!')
        programa()
print('Bem-vindo ao programa que calcula a área de um polígono regular.')
programa()