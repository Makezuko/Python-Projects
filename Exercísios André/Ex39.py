import math

def linhas():
    print('='*90)

while True:
    try:
        linhas()
        a = float(input('Insira o coeficiente A: '))
        b = float(input('Insira o coeficiente B: '))
        c = float(input('Insira o coeficiente C: '))
        delta = b**2 - 4*a*c
        if delta < 0:
            linhas()
            print('A equação não possui raízes reais.')
        elif delta == 0:
            linhas()
            raiz = -b / (2*a)
            print('A equação possui uma única raiz, {}'.format(raiz))
        else:
            linhas()
            raiz_a = (-b + math.sqrt(delta)) / (2*a)  
            raiz_b = (-b - math.sqrt(delta)) / (2*a)  
            print('As raizes da equação são: {:.2f} e {:.2f}'.format(raiz_a, raiz_b))
    except ValueError:
        linhas()
        print('Erro! Os valores inseridos precisam ser numéricos.')