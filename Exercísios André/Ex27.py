def programa():
    try:
        A = float(input('Insira o valor do coeficiente A em cm: '))
        B = float(input('Insira o valor do coeficiente B en cm: '))
        X = -B/A
        calc = A*X + B 
        if calc == 0:
            print('Uma equação de grau com coeficientes A {:.2f}cm e B {:.2f}cm existe.'.format(A, B))
            print('O valor de X é {:.2f}cm'.format(X))
    except ValueError:
        print('Erro! Os valores inseridos precisam ser numéricos.')
        programa()
print('Bem-vindo ao programa para calcular uma equação de primeiro grau.')
programa()