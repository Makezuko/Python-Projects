input_possivel = [0, 1, 2, 3, 4, 5]
exercicios = {
    0: 'Área de triângulos',
    1: 'Área de quadrados',
    2: 'Área de um retângulo',
    3: 'Área de um Paralelogramo',
    4: 'Área de um trapézio',
    5: 'Área de um círculo'
}

while True:
    try:
        print('Os exercícios disponíveis são: \n{}'.format(exercicios))    
        exercicio_escolhido = int(input('Insira que tipo de exercício você quer fazer: '))
        if exercicio_escolhido not in input_possivel:
            print('Erro! Você precisa inserir um dos exercícios possíveis.')
        else:
            print('Você escolheu {}'.format(exercicios[exercicio_escolhido]))
            break
    except ValueError:
        print('Erro! Você precisa inserir valores numéricos.')

def area_de_triangulos():
    while True:
        try:
            base = float(input('Insira o valor da base do triângulo em cm: '))
            altura = float(input('Insiria o valor da altura do triângulo em cm: '))
            if base <= 0 or altura <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            else:
                area = (base * altura)/2
                print('O valor da área de um triângulo com base {:.2f}cm e altura {:.2f}cm é de {:.2f}cm quadrados.'.format(base, altura, area))
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

def area_de_quadrados():
    while True:
        try:
            lado = float(input('Insira o valor do lado do quadrado em cm: '))
            if lado <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            else:
                area = lado**2
                print('O valor da área de um quadrado de lado {:.2f}cm é de {:.2f}cm quadrados'.format(lado, area))
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

def area_de_retangulos():
    while True:
        try:
            base = float(input('Insira o valor da base do retângulo em cm: '))
            altura = float(input('Insiria o valor da altura do triângulo em cm: '))
            if base <= 0 or altura <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            else:
                area = (base * altura)/2
                print('O valor da área de um retângulo com base {:.2f}cm e altura {:.2f}cm é de {:.2f}cm quadrados.'.format(base, altura, area))
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

def area_de_paralelogramos():
    while True:
        try:
            diagonalMaior = float(input('Insira o valor da maior diagonal do paralelogramo em cm: '))
            diagonalMenor = float(input('Insira o valor da menor diagonal do paralelogramo em cm: '))
            if diagonalMaior <= 0 or diagonalMenor <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            else:
                area = (diagonalMenor * diagonalMaior)/2
            print('O valor da área de um paralelogramo de diametros {:.2f}cm e {:.2f}cm é de {:.2f}cm quadrados'.format(diagonalMenor, diagonalMaior, area))
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

def area_de_trapezios():
    while True:
        try:
            baseM = float(input('Insira o valor da maior base do trapézio em cm: '))
            basem = float(input('Insira o valor da menor base do trapézio en cm: '))
            altura = float(input('Insira o valor da altura do trapézio em cm: '))
            if baseM <= 0 or basem <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            if baseM > basem:
                print('Erro! A base menor não pode ser maior que a maior base.')
            else:
                area = ((baseM + basem)*altura)/2
                print('O valor da área de um trapézio de bases {:.2f}cm e {:.2f}cm, com {:.2f}cm de altura é de {:.2f}cm quadrados'.format(baseM, basem, altura, area))
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

def area_de_circulo():
    while True:
        try:
            raio = float(input('Insira o valor do raio do circulo em cm: '))
            if raio <= 0:
                print('Erro! Distâncias não podem ser negativas ou nulas.')
            else:
                area = (raio**2)*3.1415
                print('O valor da área de um circulo de raio {:.2f}cm é de {:.2f}cm quadrados.'.format(raio, area)) 
        except ValueError:
            print('Erro! Você deve inserir somente valores numéricos.')

lista_de_exercicios = [area_de_triangulos(), area_de_quadrados(), area_de_retangulos(), area_de_paralelogramos(), area_de_trapezios(), area_de_circulo()]

lista_de_exercicios(exercicio_escolhido)