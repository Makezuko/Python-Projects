lista = []
soma = 0

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

for c in range(5):
    soma = soma + lista[0]
    lista.pop(0)

print('A média da lista é {}'.format(soma/2))  