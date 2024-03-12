def programa2():
    try:
        print('='*75)
        F = float(input('Insira a temperatura em Fahrenheit que deseja converter a Celsius: '))
        print('='*75)
        C = 5/9 *(F-32)
        print('{:.2f}°F são aproximadamente {:.2f}°C'.format(F, C))
        print('='*75)
    except ValueError:      
        print('='*75)
        print('Erro! Você precisa inserir uma temperatura em valores numéricos.') 
        programa2()
    print('='*75)