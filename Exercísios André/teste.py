def perimetro_de_trapezio():
    while True:
        input_possivel = [0, 1, 2]
        tipos_triângulo = {
            0: 'Escaleno',
            1: 'Isósceles',
            2: 'Retângulo',
        }
        try:
            print('Os tipos de triângulo são: {}'.format(tipos_triângulo))
            input_usuario = int(input('Insira que tipo de triângulo você quer usar: '))
            if input_usuario not in input_possivel:
                print('Erro! Você precisa inserir uma das opções disponíveis.')
            else:
                break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')

    def escaleno():
        while True:
            try:
                print('Você escolheu o trapézio escaleno.')
                base_maior = float(input('Digite o valor da maior base em cm: '))
                base_menor = float(input('Digite o valor da menor base em cm: '))
                paralelo_maior = float(input('Digite o valor do maior paralelo em cm: '))
                paralelo_menor = float(input('Digite o valor do menor paralelo em cm: '))
                if base_maior <= 0 or base_menor <= 0 or paralelo_maior <= 0 or paralelo_menor <= 0:
                    print('Erro! Distâncias não podem ser um valor negativo ou nulo.')
                else:
                    perimetro = base_maior + base_menor + paralelo_maior + paralelo_menor
                    print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
                    break
            except ValueError:
                print('Erro! Você precisa inserir valores numéricos.')           
    def isosceles():
        while True:
            try:
                print('Você escolheu o trapézio isósceles.')
                base_maior = float(input('Digite o valor da maior base em cm: '))
                base_menor = float(input('Digite o valor da menor base em cm: '))
                paralelo = float(input('Digite o valor do paralelo em cm: '))
                if base_maior <= 0 or base_menor <= 0 or paralelo <= 0:
                    print('Erro! Distâncias não podem ser um valor negativo ou nulo.')
                else:
                    perimetro = base_maior + base_menor + paralelo*2
                print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
                break
            except ValueError:
                print('Erro! Você precisa inserir valores numéricos.')
    def retangulo():
        while True:
            try:
                print('Você escolheu o trapézio retângulo.')
                base_maior = float(input('Digite o valor da maior base em cm: '))
                base_menor = float(input('Digite o valor da menor base em cm: '))
                paralelo_maior = float(input('Digite o valor do maior paralelo em cm: '))
                paralelo_menor = float(input('Digite o valor do menor paralelo em cm: '))
                if base_maior <= 0 or base_menor <= 0 or paralelo_maior <= 0 or paralelo_menor <= 0:
                    print('Erro! Distâncias não podem ser um valor negativo ou nulo.')
                else:
                    perimetro = base_maior + base_menor + paralelo_maior + paralelo_menor
                    print('O valor do perímetro deste trapézio é de {}cm'.format(perimetro))
                    break
            except:
                print('Erro! Você precisa inserir valores numéricos.')
    
    if input_usuario == 0:
        escaleno()
    elif input_usuario == 1:
        isosceles()
    elif input_usuario == 2:
        retangulo()

perimetro_de_trapezio()