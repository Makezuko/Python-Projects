def programa():
    try:
        print('='*75)
        C = float(input('Insira a temperatura em Celsius que deseja converter a Fahrenheit: '))
        print('='*75)
        F = (C * 1.8) + 32
        print('{:.2f}°C são aproximadamente {:.2f}°F'.format(C, F))
        print('='*75)
    except ValueError:      
        print('='*75)
        print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
        programa()
programa()