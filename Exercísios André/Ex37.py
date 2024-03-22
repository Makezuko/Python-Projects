def linhas():
    print('='*85)

while True:
    try:
        linhas()
        angulo_x = float(input('Insira o valor do primeiro ângulo: '))
        angulo_y = float(input('Insira o valor do segundo ângulo: '))
        angulo_z = float(input('Insira o valor do terceiro ângulo: '))
        if angulo_x <= 0 \
        or angulo_y <= 0 \
        or angulo_z <= 0:
            linhas()
            print('Erro! Ângulos não podem receber valores negativos ou nulos.')
        elif angulo_x + angulo_y + angulo_z != 180:
            linhas()
            print('Erro! Não pode existir um triângulo onde a soma dos seus ângulos é diferente de 180.')
        elif (angulo_x > 90 and angulo_y < 90 and angulo_z < 90) \
        or (angulo_y > 90 and angulo_x < 90 and angulo_z < 90) \
        or (angulo_z > 90 and angulo_x < 90 and angulo_y < 90):
            linhas()
            print('O Triângulo é obtusângulo.')
        elif (angulo_x == 90 and angulo_y == angulo_z) \
        or (angulo_y == 90 and angulo_x == angulo_z) \
        or (angulo_z == 90 and angulo_x == angulo_y):
            linhas()
            print('O Triângulo é retângulo.')
        elif angulo_x < 90 and angulo_y < 90 and angulo_z < 90:
            linhas()
            print('O Triângulo é acutâgulo.')

    except ValueError:
        linhas()
        print('Erro! Você precisa inserir valores numéricos.')