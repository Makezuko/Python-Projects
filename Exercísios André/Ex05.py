def programa5():
    try:
        print('='*75)
        C = float(input('Insira a temperatura em Celsius que deseja converter a Rankine: '))
        print('='*75)
        R = (C + 273.15)*(9/5)
        print('{:.2f}°C são aproximadamente {:.2f}°R'.format(C,R))
    except ValueError:      
        print('='*75)
        print('Erro! Você precisa inserir uma temperatura em valores numéricos.')
        programa5() 
    print('='*75)
