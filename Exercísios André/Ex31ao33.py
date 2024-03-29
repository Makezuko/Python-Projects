import random

qtd_numeros = int(input('Insira quantos números aleatórios o computador irá comparar: '))

numeros_aleatorios = []

for _ in range (qtd_numeros):
    while True:
        numero_aleatorio = random.randrange(0, 500)
        if numero_aleatorio not in numeros_aleatorios:
            numeros_aleatorios.append(numero_aleatorio)
            break

def arrange():
    for x in range(qtd_numeros):
        menor_indice = x
        for j in range(x + 1, qtd_numeros):
            if numeros_aleatorios[j] < numeros_aleatorios[menor_indice]:
                menor_indice = j
        numeros_aleatorios[x], numeros_aleatorios[menor_indice] = numeros_aleatorios[menor_indice], numeros_aleatorios[x]

arrange()
print(numeros_aleatorios)