try:
    print('='*75)
    K = float(input('Insira a temperatura em Kelvin que deseja converter a Celsius: '))
    print('='*75)
    C = K - 273.15
    print('{:.2f}°K são aproximadamente {:.2f}°C'.format(K, C))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)