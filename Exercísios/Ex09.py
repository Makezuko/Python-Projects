import random
import math

inteiro_a = float(random.randrange(-10, 10))
inteiro_b = float(random.randrange(-10, 10))
real = float(input('Insira um número real ou seu valor aproximado: '))

ex1 = (inteiro_a * 2) + (inteiro_b / 2)
ex2 = (inteiro_a * 3) + real
ex3 = (real**3)

print('Inteiro A: {:.2f}'.format(inteiro_a))
print('Inteiro B: {:.2f}'.format(inteiro_b))
print('Real: {:.2f}'.format(real))
print('Ex1: {:.2f}'.format(ex1))
print('Ex2: {:.2f}'.format(ex2))
print('Ex3: {:.2f}'.format(ex3))