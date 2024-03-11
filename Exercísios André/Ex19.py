def programa():
    try:
        base = float(input('Insira o valor da base do triângulo em cm: '))
        if base <= 0:
            print('Erro! Você precisa inserir um valor positivo.')
            programa()
        if base > 0:
            altura = float(input('Insiria o valor da base do triângulo em cm: '))
            while altura <= 0:
                print('Erro! Você precisa inserir um valor positivo.')
                altura = float(input('Insiria o valor da base do triângulo em cm: '))
            if altura > 0:
                area = (base * altura)/2
                print('O valor da área de um triângulo com base {:.2f}cm e altura {:.2f}cm é de {:.2f}cm quadrados.'.format(base, altura, area))
    except ValueError:
        print('Erro! Você precisa inserir um valor numérico.')
        programa()
print('Bem-vindo ao programa de área de um triângulo')
programa()