def programa():
    try:
        lado = float(input('Insira o valor do lado do um retângulo em cm: '))
        while lado <= 0:
            print('Erro! O valor do lado precisa ser positivo.')
            lado = float(input('Insira o valor do lado do retângulo em cm: '))
        if lado > 0:
            base = float(input('Insira o valor da base do retângulo em cm: '))
            while base <= 0: 
                print('Erro! O valor do lado precisa ser positivo.')
                base = float(input('Insira o valor da base do retângulo em cm: '))
            if base > 0:
                area = base * lado
                print('O valor da área de um retângulo de lado {:.2f}cm e base {:.2f}cm é de {:.2f}cm'.format(lado, base, area))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico.')
        programa()
print('Bem-vindo ao programa de área de um retângulo')
programa()