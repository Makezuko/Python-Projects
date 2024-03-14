temperatura = [0, 1, 2, 3]

try:
    print('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3)')
    matriz_a = int(input('Insira que temperatura você deseja converter: '))
    matriz_b = int(input('Insira a temperatura a qual você deseja converter: '))
    while matriz_a not in temperatura or matriz_b not in temperatura:
        print('Erro! Você precisa inserir um dos valores pedidos')
        print('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3)')
        matriz_a = int(input('Insira que temperatura você deseja converter: '))
        matriz_b = int(input('Insira a temperatura a qual você deseja converter: '))
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

def _celsiusParaFahrenheit(x):
    return (x * 9/5) + 32

def _celsiusParaKelvin(x):
    return x + 273.15

def _celsiusParaRankine(x):
    return (x + 273.15)*(9/5)
    
def _fahrenheitParaCelsius(x):
    return (x - 32) * 5/9
    
def _fahrenheitParaKelvin(x):
    return (x + 459.67) * 5/9
    
def _fahrenheitParaRankine(x):
    return (x + 459.67)
    
def _kelvinParaCelsius(x):
    return (x - 273.15)
    
def _kelvinParaFahrenheit(x):
    return (x - 273.15) * (5/9) + 32
    
def _kelvinParaRankine(x):
    return x * (9/5)
    
def _rankineParaCelsius(x):
    return (x - 491.67) * (5/9)
    
def _rankineParaFahrenheit(x):
    return x - 459.67
    
def _rankineParaKelvin(x):
    return x / (9/5)

conversão = [
        # Celsius             Farenheigt               Kelvin              Rankine
        ['As Escalas são iguais', _celsiusParaFahrenheit(x), _celsiusParaKelvin(x), _celsiusParaRankine(x)],            # Celsius
        [_fahrenheitParaCelsius(x), 'As Escalas são iguais', _fahrenheitParaKelvin(x), _fahrenheitParaRankine(x)],     # Farenheit
        [_kelvinParaCelsius(x), _kelvinParaFahrenheit(x), 'As Escalas são iguais', _kelvinParaRankine(x)],             # Kelvin
        [_rankineParaCelsius(x), _rankineParaFahrenheit(x), _rankineParaKelvin(x), 'As Escalas são iguais']            # Rankine
    ]
try:
    print('{:.2f}°{} é aproximadamente {:.2f}°{}'.format(x, escala_a, conversão[matriz_a][matriz_b], escala_b))
except ValueError:
    print(conversão[matriz_a][matriz_b])
    print('{:.2f}°{} é igual a {:.2f}°{}'.format(x, escala_a, x, escala_b))