def programa():
    try:
        lado1 = float(input('Insira um lado de um triângulo em cm: '))
        lado2 = float(input('Insira outro lado do mesmo triângulo em cm: '))
        lado3 = float(input('Insira o outro lado do mesmo triângulo em cm: '))
        while lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            print('Erro! \nVocê precisa inserir um valor positivo, já que não existem triângulos com valores negativos ou nulos.')
            lado1 = float(input('Insira um lado de um triângulo em cm: '))
            lado2 = float(input('Insira outro lado do mesmo triângulo em cm: '))
            lado3 = float(input('Insira o outro lado do mesmo triângulo em cm: '))
        while lado1+lado2 <= lado3 or lado2+lado3 <= lado1 or lado1+lado3 <= lado2:
            print('Erro! \nPara um triângulo existir o valor da soma dos dois menores lados de um triângulo não pode ser menor ou igual ao lado maior.')
            lado1 = float(input('Insira um lado de um triângulo em cm: '))
            lado2 = float(input('Insira outro lado do mesmo triângulo em cm: '))
            lado3 = float(input('Insira o outro lado do mesmo triângulo em cm: '))
        else:
            perimetro = lado1 + lado2 + lado3
            print('O perímetro de um triângulo de lados {:.2f}cm {:.2f}cm e {:.2f}cm é de aproximadamente {:.2f}cm'.format(lado1, lado2, lado3, perimetro))       
    except ValueError:
        print('Erro! \nVocê precisa inserir um valor numérico.')
        programa()
        
programa()