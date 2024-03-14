try:
    print('Celsius (0), Fahrenheit (1), Kelvin (2) ou Rankine (3)')
    matriz_a = int(input('Insira que temperatura você deseja converter: '))
    matriz_b = int(input('Insira a temperatura a qual você deseja converter: '))
    while 0 > matriz_a or matriz_a > 3 or 0 > matriz_b or matriz_b > 3:
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

def _celsiusParaFahrenheit():
    return (x * 9/5) + 32

def _celsiusParaKelvin():
    return x + 273.15

def _celsiusParaRankine():
    return (x + 273.15)*(9/5)
    
def _fahrenheitParaCelsius():
    return (x - 32) * 5/9
    
def _fahrenheitParaKelvin():
    return (x + 459.67) * 5/9
    
def _fahrenheitParaRankine():
    return (x + 459.67)
    
def _kelvinParaCelsius():
    return (x - 273.15)
    
def _kelvinParaFahrenheit():
    return (x - 273.15) * (5/9) + 32
    
def _kelvinParaRankine():
    return x * (9/5)
    
def _rankineParaCelsius():
    return (x - 491.67) * (5/9)
    
def _rankineParaFahrenheit():
    return x - 459.67
    
def _rankineParaKelvin():
    return x / (9/5)

conversão = [
        # Celsius             Farenheigt               Kelvin              Rankine
        ['As Escalas são iguais', _celsiusParaFahrenheit(), _celsiusParaKelvin(), _celsiusParaRankine()],            # Celsius
        [_fahrenheitParaCelsius(), 'As Escalas são iguais', _fahrenheitParaKelvin(), _fahrenheitParaRankine()],     # Farenheit
        [_kelvinParaCelsius(), _kelvinParaFahrenheit(), 'As Escalas são iguais', _kelvinParaRankine()],             # Kelvin
        [_rankineParaCelsius(), _rankineParaFahrenheit(), _rankineParaKelvin(), 'As Escalas são iguais']            # Rankine
    ]
try:
    print('{:.2f}°{} é aproximadamente {:.2f}°{}'.format(x, escala_a, conversão[matriz_a][matriz_b], escala_b))
except ValueError:
    print(conversão[matriz_a][matriz_b])
    print('{:.2f}°{} é igual a {:.2f}°{}'.format(x, escala_a, x, escala_b))