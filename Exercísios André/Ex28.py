from Ex01 import programa1
from Ex02 import programa2
from Ex03 import programa3
from Ex04 import programa4
from Ex05 import programa5
from Ex06 import programa6
from Ex07 import programa7
from Ex08 import programa8
from Ex09 import programa9
from Ex10 import programa10
from Ex11 import programa11
from Ex12 import programa12

def programa():
    try:
        print('='*75)
        print("Bem-vindo ao programa que calcula diferentes tipos de temperaturas.")
        print("Qual a temperatura que você deseja converter?")
        print('='*75)
        temperatura_a_converter = int(input("Celsius (1), Fahrenheit (2), Kelvin (3), Rankine (4): "))
        print('='*75)
        while temperatura_a_converter <= 0 or temperatura_a_converter > 4:
            print("Erro! Por favor insira um dos valores pedidos.")
            print('='*75)
            print("Qual a temperatura que você deseja converter?")
            temperatura_a_converter = int(input("Celsius (1), Fahrenheit (2), Kelvin (3), Rankine (4): "))
        print("A qual temperatura que você deseja converter?")
        temperatura_a_ser_convertida = int(input("Celsius (1), Fahrenheit (2), Kelvin (3), Rankine (4): "))
        while temperatura_a_ser_convertida <= 0 or temperatura_a_ser_convertida > 4:
            print("Erro! Por favor insira um dos valores pedidos.")
            print('='*75)
            print("A Qual temperatura que você deseja converter?")
            print('='*75)
            temperatura_a_ser_convertida = int(input("Celsius (1), Fahrenheit (2), Kelvin (3), Rankine (4): "))
        if temperatura_a_converter == temperatura_a_ser_convertida:
            print("Erro! Para o programa funcionar escolha 2 escalas de temperatura diferentes.")
            programa()
        if temperatura_a_converter == 1 and temperatura_a_ser_convertida == 2:
            programa1()
        if temperatura_a_converter == 1 and temperatura_a_ser_convertida == 3:
            programa3()
        if temperatura_a_converter == 1 and temperatura_a_ser_convertida == 4:
            programa5()
        if temperatura_a_converter == 2 and temperatura_a_ser_convertida == 1:
            programa2()
        if temperatura_a_converter == 2 and temperatura_a_ser_convertida == 3:
            programa7()
        if temperatura_a_converter == 2 and temperatura_a_ser_convertida == 4:
            programa9()
        if temperatura_a_converter == 3 and temperatura_a_ser_convertida == 1:
            programa4()
        if temperatura_a_converter == 3 and temperatura_a_ser_convertida == 2:
            programa8()
        if temperatura_a_converter == 3 and temperatura_a_ser_convertida == 4:
            programa11()
        if temperatura_a_converter == 4 and temperatura_a_ser_convertida == 1:
            programa6()
        if temperatura_a_converter == 4 and temperatura_a_ser_convertida == 2:
            programa10()
        if temperatura_a_converter == 4 and temperatura_a_ser_convertida == 3:
            programa12()
    except ValueError:
        print("Erro! Os valores inseridos devem ser numéricos")
        programa()
#programa()


class Temperatura:

    CELSIUS = 0
    FARENHEIT = 1
    KELVIN = 2
    RANKINE = 3

    def _identidade(X):
        return X
    
    def _celsiusParaFarenheit(x):
        return x*9/5 + 32

    conversão = [
        # Celsius   Farenheigt  Kelvin  Rankine
        [_identidade, _celsiusParaFarenheit, programa3, programa5],   # Celsius
        [programa2, _identidade, programa7, programa9],              # Farenheit
        [programa4, programa8, _identidade, programa11],             # Kelvin
        [programa6, programa10, programa12, _identidade]             # Rankine
    ]

z = 100

obj = Temperatura()
print(f"{z} celsius = {obj.conversão[Temperatura.CELSIUS][Temperatura.CELSIUS](z)} celsius")