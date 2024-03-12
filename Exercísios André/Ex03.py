def programa3():
    try:
        print('='*75)
        C = float(input('Insira a temperatura em Celsius que deseja converter a Kelvin: '))
        print('='*75)
        K = C + 273.15
        if K < 0:
            print("Erro! Os valores Kelvin não podem ser negativos")
            programa3()
        else:
            print('{:.2f}°C são aproximadamente {:.2f}°K'.format(C, K))
    except ValueError:      
        print('='*75)
        print('Erro! Você precisa inserir uma temperatura em valores numéricos.')
        programa3() 
    print('='*75)