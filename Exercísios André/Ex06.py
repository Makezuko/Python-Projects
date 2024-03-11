try:
    print('='*75)
    R = float(input('Insira a temperatura em Rankine que deseja converter a Celsius: '))
    print('='*75)
    C = (R - 491.67) * (5/9)
    print('{:.2f}°R são aproximadamente {:.2f}°C'.format(R, C))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)