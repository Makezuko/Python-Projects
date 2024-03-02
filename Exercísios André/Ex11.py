try:
    print('='*75)
    K = float(input('Insira a temperatura em Kelvin que deseja converter a Rankine: ')) 
    print('='*75)
    R = ((K - 273.15) * 1.8) + 491.67
    print('{:.2f}°K são aproximadamente {:.2f}°R'.format(K, R))
except ValueError:      
    print('='*75)
    print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
print('='*75)