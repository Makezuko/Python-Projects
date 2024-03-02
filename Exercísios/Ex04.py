import math

raio = float(input('Insira o Valor do raio do círculo em centímetros: '))
calc = math.pi * (raio**2)
print('A área de um círculo de raio {:.2f}cm é de aproximadamente {:.2f}cm'.format(raio, calc)) 