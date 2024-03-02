import random
import math

area = float(random.uniform(0, 100))
print('{:.2f}'.format(area))

litros = area / 3
print('{:.2f}'.format(litros))
litro_lata = 18
min_latas = litros / litro_lata
print('{:.2f}'.format(math.ceil(min_latas)))
valor_total = min_latas * 80
print('O valor total é de {:.2f}, já que são necessárias {} latas para pintar {:.2f}m quadrados'.format(valor_total, math.ceil(min_latas), area))