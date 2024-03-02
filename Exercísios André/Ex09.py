try:
    print('='*75)
    F = float(input('Insira a temperatura em Fahrenheit que deseja converter a Rankine: ')) 
    print('='*75)
    C = 5/9 *(F-32)
    R = (C + 273.15)*(9/5)
    print('{:.2f}°F são aproximadamente {:.2f}°R'.format(F, R))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)