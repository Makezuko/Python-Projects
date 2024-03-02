#Faça um Programa que peça dois números e imprima o maior deles.
from random import randrange

a = randrange(-10, 10)
b = randrange(-10, 10)
while a == b:
    b = randrange(-10, 10)

print('a = {}'.format(a))
print('b = {}'.format(b))

if a > b:
    print('O valor {} é maior que o valor {}'.format(a, b))
if b > a:
    print('O valor {} é maior que o valor {}'.format(b, a))
