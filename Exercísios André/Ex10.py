try:
    print('='*75)
    R = float(input('Insira a temperatura em Rankine que deseja converter a Fahrenheit: ')) 
    print('='*75)
    F =  (R - 459.67)
    print('{:.2f}°R são aproximadamente {:.2f}°F'.format(R, F))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)