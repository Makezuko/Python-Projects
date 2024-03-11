def programa():
    try:
        lado = float(input('Insira o valor do lado do quadrado em cm: '))
        if lado <= 0:
            print('Erro! O valor do lado precisa ser positivo.')
            programa()
        if lado > 0:
            area = lado**2
            print('O valor da área de um quadrado de lado {:.2f}cm é de {:.2f}cm quadrados'.format(lado, area))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico.')
        programa()
print('Bem-vindo ao programa de área de um quadrado')
programa()