lista = []

for c in range(5):
    while True:
        try:
            numero = float(input('Insira um número: '))
            if numero in lista:
                print('Erro! Insira um número que não esteja na lista.')
            else:
                lista.append(numero)
                break
        except ValueError:
            print('Erro! Você precisa inserir valores numéricos')

print('Os números analisados serão: {}'.format(lista))

while len(lista) > 1:
    try:
        if lista[0] > lista[1]: 
            lista.pop(0)
        if lista[1] > lista[0]:         
            lista.pop(1)
    except IndexError:
        break

print('O menor número da lista é {}'.format(lista[0]))
