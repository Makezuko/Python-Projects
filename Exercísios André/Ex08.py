try:
    print('='*75)
    K = float(input('Insira a temperatura em Kelvin que deseja converter a Fahrenheit: '))
    while K < 0:
        print("Os valores Kelvin não podem ser menores que 0")
        K = float(input('Insira a temperatura em Kelvin que deseja converter a Fahrenheit: '))
    print('='*75)
    C = K - 273.15
    F = (C * 1.8) + 32
    print('{:.2f}°K são aproximadamente {:.2f}°F'.format(K, F))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)