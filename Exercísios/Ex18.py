# Descobrir os valores ímpares dentro de um range de númeross inteiros

n = int(input('Insira o valor mínimo: '))
a = int(input('Insira um valor máximo: '))
b = a+1

for n in range(n+1  , b):
    if n % 2 != 0:                      #if n % 2 == 0: Para descobrir números pares
        print(n)    