while True:
    try:
        tamanho = int(input('Insira o tamanho do quadrado a ser criado: '))
        if tamanho <= 1:
            print('Erro! O valor escolhido deve ser um número inteiro maior que 1.')
        else:
            break
    except ValueError:
        print('Erro!')

for i in range(tamanho):
        for j in range(tamanho):
            if i == 0 or i == tamanho - 1 or j == 0 or j == tamanho - 1:
                print('*', end='')              
            else:
                print(' ', end='')
        print(' ')