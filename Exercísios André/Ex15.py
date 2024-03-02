def programa():
    try:
        print('-'*75)
        lado1 = float(input('Insira o valor de um dos paralelos em cm: '))
        lado2 = float(input('Insira o valor de outro paralelo diferente em cm: '))
        print('-'*75)
        while lado1 <= 0 or lado2 <=0:
            print('Erro! Você precisa inserir valores maiores a 0, já que não existem distâncias negativas ou nulas.')
            programa()
        perimetro = 2*(lado1 + lado2)
        print('O perímetro de um paralelogramo da lados {:.2f}cm e {:.2f}cm é {:.2f}cm'.format(lado1, lado2, perimetro))
        restart()              
    except ValueError:
        print('Erro! Você precisa inserir valores numéricos')
        programa()

def restart():
    try:
        print('-'*75)
        replay = int(input('Você quer descobrir o perímetro de outro paralelogramo? Sim(1), Não(2): '))
        if replay == 1:
            programa()
        if replay == 2:
            print('-'*75)
            print('Obrigado por usar este programa!')
            print('-'*75)
            exit()
        while replay != 1 and replay != 2:
            print('-'*75)
            print('Erro! Você precisa inserir um dos valores pedidos.')
            restart()
    except ValueError:
        print('-'*75)
        print('Erro! Você precisa inserir valores numéricos')
        restart()
print('-'*75)

def start():
    print('Seja bem-vindo/a ao programa para calcular o perímetro de paralelogramos.')
    programa()

start()