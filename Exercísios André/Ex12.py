try:
    print('='*75)
    R = float(input('Insira a temperatura em Rankine que deseja converter a Kelvin: ')) 
    print('='*75)
    K = ((R - 491.67) / 1.79999999) + 273.15
    print('{:.2f}°R são aproximadamente {:.2f}°K'.format(R, K))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)