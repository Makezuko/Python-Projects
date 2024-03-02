def programa():
    try:
        lado1 = float(input('Insira um lado de um quadrado em cm: '))
        while lado1 <= 0:
            print('Erro! \nVocê precisa inserir um valor positivo, já que não existem quadrados com valores negativos ou nulos.')
            lado1 = float(input('Insira um lado de um quadrado em cm: '))
        else:
            perimetro = lado1*4
            print('O perímetro de um quadrado com {:.2f}cm de lado, é de aproximadamente {:.2f}cm'.format(lado1, perimetro))
            quit()       
    except ValueError:
        print('Erro! \nVocê precisa inserir um valor numérico.')
        programa()
        
programa()