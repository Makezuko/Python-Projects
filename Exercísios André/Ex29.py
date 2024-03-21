input_possivel = [0, 1, 2, 3, 4, 5]

exercicios = {
    0: 'Perímetro de triângulos',
    1: 'Perímetro de quadrado/losango',
    2: 'Perímetro de retângulo/paralelogramo',
    3: 'Perímetro de um trapézio',
    4: 'Perímetro de poligono regular',
    5: 'Perímetro de um círculo'
}

while True:
    try:
        print('Os exercícios disponíveis são: {}'.format(exercicios))
        input_exercicio = int(input('Insira o tipo de cálculo que você quer fazer: '))
        if input_exercicio not in input_possivel:
            print('Erro! Você precisa inserir uma das opções disponíveis')
        else:
            break
    except ValueError:
        print('Erro! Você precisa inserir uma das possibilidades citadas pelo seu valor numérico.')

def perimetro_de_triangulo():
    while True:
        try:
            lado1 = float(input('Insira um lado de um triângulo em cm: '))
            lado2 = float(input('Insira outro lado do mesmo triângulo em cm: '))
            lado3 = float(input('Insira o outro lado do mesmo triângulo em cm: '))
            if lado1 <= 0 or lado2 <=0 or lado3 <= 0:
                print('Erro! Distâncias não podem ser nulas ou negativas.')
            elif lado1+lado2 <= lado3 or lado2+lado3 <= lado1 or lado1+lado3 <= lado2:
                print('Erro! Para um triângulo existir é necessário que os dois lados menores somados sejam maiores que o maior lado.')
            else:
                perimetro = lado1 + lado2 + lado3
                print('O perímetro de um triângulo de lados {:.2f}cm {:.2f}cm e {:.2f}cm é de aproximadamente {:.2f}cm'.format(lado1, lado2, lado3, perimetro))
                break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')  

def perimetro_de_quadrado():
    while True:
        try:
            lado = float(input('Insira o valor de um dos lados do quadrado em cm: '))
            if lado <= 0:
                print('Erro! Distâncias não podem ser nulas ou negativas')
            else:
                perimetro = lado*4
                print('O perímetro de um quadrado com {:.2f}cm de lado, é de aproximadamente {:.2f}cm'.format(lado, perimetro))
                break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')

def perimetro_de_paralelogramo():
    while True:
        try:
            lado1 = float(input('Insira o valor de um dos paralelos em cm: '))
            lado2 = float(input('Insira o valor de outro paralelo diferente em cm: ')) 
            if lado1 <= 0 or lado2 <= 0:
                print('Erro! Distâncias não podem ser nulas ou negativas')
            else:
                perimetro = 2*(lado1 + lado2)
                print('O perímetro de um paralelogramo da lados {:.2f}cm e {:.2f}cm é {:.2f}cm'.format(lado1, lado2, perimetro))
                break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')

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

def perimetro_de_poligono_regular():
    while True:
        try:
            lados = int(input('Insira a quantidade de lados que o polígono regular possui: '))
            if lados < 3:
                print('Erro! Para que um polígono exista é necessário que ele tenha pelo menos 3 lados.')
            valor_lados = float(input('Insira o valor de um dos lados do polígono em cm: '))
            perimetro = lados * valor_lados
            print('O valor do perímetro de um polígono regular de {} lados de {:.2f}cm é de {:.2f}cm'.format(lados, valor_lados, perimetro))
            break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')
        
def perimetro_de_circulo():
    while True:
        try:
            raio = float(input('Insira o valor do raio do circulo em cm: '))
            if raio <= 0:
                print('Erro! Distâncias não podem ser um valor negativo ou nulo.')
            perimetro = raio * (3.1415 * 2)
            print('O valor do perimetro de um circulo de raio {:.2f}cm é igual a {}cm'.format(raio, perimetro))
            break
        except ValueError:
            print('Erro! Você precisa inserir um valor numérico.')

lista = [perimetro_de_triangulo, perimetro_de_quadrado, perimetro_de_paralelogramo, perimetro_de_trapezio, perimetro_de_poligono_regular, perimetro_de_circulo]
exercicio_escolhido = lista[input_exercicio]
exercicio_escolhido()