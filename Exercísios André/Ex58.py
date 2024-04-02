lista_opcoes = ('Quadrado completo', 'Quadrado vazio')
lista = {
    0:'Quadrado completo',
    1:'Quadrado vazio'
}

print(lista)
escolha = int(input('Insira que tipo de quadrado você quer fazer: '))

while True:
    try:
        
        tamanho = int(input('Insira o tamanho do quadrado a ser criado: '))
        if tamanho <= 1:
            print('Erro! O valor escolhido deve ser um número inteiro maior que 1.')
        else:   
            break
    except ValueError:
        print('Erro!')

if escolha in lista:
    if escolha == 1:
        for i in range(tamanho):
            for j in range(tamanho):
                if i == 0 or i == tamanho - 1 or j == 0 or j == tamanho - 1:
                    print('*', end='')              
                else:
                    print(' ', end='')
            print(' ')
    if escolha == 0:
        for i in range(tamanho):
            for j in range(tamanho):
                print('*', end='')              
            print(' ')
