try:
    print('Insira que temperatura você deseja converter.')
    matriz_a = int(input('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3): '))
    print('Insira a temperatura a qual você deseja converter')
    matriz_b = int(input('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3): '))
    while 0 > matriz_a or matriz_a > 3 or 0 > matriz_b or matriz_b > 3:
        print('Erro! Você precisa inserir um dos valores pedidos')
        print('Insira que temperatura você deseja converter.')
        matriz_a = int(input('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3): '))
        print('Insira a temperatura a qual você deseja converter')
        matriz_b = int(input('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3): '))
    x = float(input('Insira o valor da temperatura a ser convertida: '))
except ValueError:
    print('Erro! Você precisa inserir valores numéricos')

if matriz_a == 0:
    escala_a = 'C'

if matriz_a == 1:
    escala_a = 'F'

if matriz_a == 2:
    escala_a = 'K' 

if matriz_a == 3:
    escala_a = 'R' 

if matriz_b == 0:
    escala_b = 'C' 

if matriz_b == 1:
    escala_b = 'F' 

if matriz_b == 2:
    escala_b = 'K' 

if matriz_b == 3:
    escala_b = 'R'     