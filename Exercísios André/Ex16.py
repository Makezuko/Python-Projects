try:
    tipo_trapezio = int(input('Qual o tipo de trapézio a ser calculado? Escaleno (1), Isósceles (2) ou Retângulo (3): '))
    while tipo_trapezio != 1 and tipo_trapezio != 2 and tipo_trapezio != 3:
        print('Erro! Você precisa inserir um dos valores pedidos.')
    if tipo_trapezio == 1:
        print('Você escolheu o trapézio escaleno.')
        base_maior = float(input('Digite o valor da maior base em cm: '))
        base_menor = float(input('Digite o valor da menor base em cm: '))
        paralelo_maior = float(input('Digite o valor do maior paralelo em cm: '))
        paralelo_menor = float(input('Digite o valor do menor paralelo em cm: '))
        perimetro = base_maior + base_menor + paralelo_maior + paralelo_menor
        print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
    elif tipo_trapezio == 2:
        print('Você escolheu o trapézio isósceles.')
        base_maior = float(input('Digite o valor da maior base em cm: '))
        base_menor = float(input('Digite o valor da menor base em cm: '))
        paralelo = float(input('Digite o valor do paralelo em cm: '))
        perimetro = base_maior + base_menor + paralelo*2
        print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
    if tipo_trapezio == 3:
        print('Você escolheu o trapézio retângulo.')
        base_maior = float(input('Digite o valor da maior base em cm: '))
        base_menor = float(input('Digite o valor da menor base em cm: '))
        paralelo_maior = float(input('Digite o valor do maior paralelo em cm: '))
        paralelo_menor = float(input('Digite o valor do menor paralelo em cm: '))
        perimetro = base_maior + base_menor + paralelo_maior + paralelo_menor
        print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
except ValueError:
    print('Erro! É preciso inserir um valor numérico em todas as respostas.')