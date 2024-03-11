def programa():
    try:
        raio = float(input('Insira o valor do raio do circulo em cm: '))
        while raio <= 0:
            print('Erro! Os valores precisam ser positivos.')
            raio = float(input('Insira o valor do raio do circulo em cm: '))
        area = (raio**2)*3.1415
        print('O valor da área de um circulo de raio {:.2f}cm é de {:.2f}cm quadrados.'.format(raio, area)) 
    except ValueError:
        print('Erro! Os valores inseridos precisam ser numéricos.')
        programa()
print('Bem-vindo ao programa para calcular a área de um circulo.')
programa()