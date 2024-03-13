class Temperatura:
    def input_usuario1():
        try:
            print('Insira qual temperatura você deseja converter.')
            matriz_a = int(input('Celsius (1), Fahrenheit (2), Kelvin (3) ou Rankine (4): '))
            print('Insira a temperatura a qual você deseja converter')
            matriz_b = int(input('Celsius (1), Fahrenheit (2), Kelvin (3) ou Rankine (4): '))
            while 0 >= matriz_a or matriz_a > 4 or 0 >= matriz_b or matriz_b > 4:
                print('Erro! Você precisa inserir um dos valores pedidos')
                print('Insira qual temperatura você deseja converter.')
                matriz_a = int(input('Celsius (1), Fahrenheit (2), Kelvin (3) ou Rankine (4): '))
                print('Insira a temperatura a qual você deseja converter')
                matriz_b = int(input('Celsius (1), Fahrenheit (2), Kelvin (3) ou Rankine (4): '))
        except ValueError:
            print('Erro! Você precisa inserir valores numéricos')
            Temperatura.input_usuario1()

    def input_usuario2():
        x = float(input('Insira o valor da temperatura a ser convertida, usando o ponto como virgula caso necessário: '))

    def _identidade(X):
        print('')
    
    def _celsiusParaFarenheit(x):
        return x * 9/5 + 32
    
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
        return (x - 273.15)  (5/9)+ 32
    
    def _kelvinParaRankine(x):
        return x * (9/5)
    
    def _rankineParaCelsius(x):
        return (x - 491.67) * (5/9)
    
    def _rankineParaFahrenheit(x):
        return x - 459.67
    
    def _rankineParaKelvin(x):
        return x * (9/5)
    
    conversão = [
        # Celsius             Farenheigt               Kelvin              Rankine
        [_identidade, _celsiusParaFarenheit, _celsiusParaKelvin, _celsiusParaRankine],            # Celsius
        [_fahrenheitParaCelsius, _identidade, _fahrenheitParaKelvin, _fahrenheitParaRankine],     # Farenheit
        [_kelvinParaCelsius, _kelvinParaFahrenheit, _identidade, _kelvinParaRankine],             # Kelvin
        [_rankineParaCelsius, _rankineParaFahrenheit, _rankineParaKelvin, _identidade]            # Rankine
    ]

Temperatura.input_usuario1()

# obj = Temperatura()
# print(f"{z} celsius = {obj.conversão[Temperatura.CELSIUS][Temperatura.CELSIUS](z)} celsius")