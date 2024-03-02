try:
    print('='*75)
    F = float(input('Insira a temperatura em Fahrenheit que deseja converter a Kelvin: ')) 
    print('='*75)
    C = 5/9 *(F-32)
    K = C + 273.15
    print('{:.2f}°F são aproximadamente {:.2f}°K'.format(F, K))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)