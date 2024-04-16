while True:
    try:
        lim1 = int(input('Insira um valor inteiro: '))
        lim2 = int(input('Insira um valor diferente: '))
        if lim2 <= lim1:
            print('Erro! O segundo valor deve ser maior que o primeiro')
        else:
            break
    except ValueError:
        print('Erro! Você precisa inserir valores numéricos.')

lista = []

for x in range(lim1, lim2):
    if x < 2:
        continue
    is_prime = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    if is_prime:
        lista.append(x)


print(lista)