def programa():
    try:
        raio = float(input('Insira o valor do raio do circulo em cm: '))
        if raio <= 0:
            print('Erro! Você precisa inserir um positivo.')
            programa()
        if raio > 0:
            perimetro = raio * (2* 3.1415)
            print('O valor do perimetro de um circulo de raio {:.2f}cm é igual a {}cm'.format(raio, perimetro))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico')
        programa()
print('Bem-vindo ao programa de cálculo de círculos ')
programa()