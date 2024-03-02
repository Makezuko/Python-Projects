from random import randrange

a = randrange(-10, 10)
print('O número escolhido foi:', a)

if a > 0:
    print('Este valor é positivo')
if a < 0:
    print('Este valor é negativo')
if a == 0:
    print('Este valor é nulo')