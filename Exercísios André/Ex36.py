def linhas():
     print('='*50)

while True:
    try:
        linhas()
        reta_a = float(input('Insira o valor da primeira reta em cm: '))
        reta_b = float(input('Insira o valor da segunda reta em cm: '))
        reta_c = float(input('Insira o valor da terceira reta em cm: '))
        if reta_a <= 0 or reta_b <= 0 or reta_c <= 0:
            linhas()
            print('Erro! Os valores não podem ser negativos ou nulos.')
        elif reta_a + reta_b > reta_c and reta_b + reta_c > reta_a and reta_a + reta_c > reta_b:
            if (reta_a == reta_b and reta_a != reta_c) or \
               (reta_a == reta_c and reta_a != reta_b) or \
               (reta_b == reta_c and reta_b != reta_a):
                linhas()
                print('O triângulo é Isósceles.')
            elif reta_a == reta_b and reta_a == reta_c:
                linhas()
                print('O triângulo é Equilátero.')
            else:
                linhas() 
                print('O triângulo é Escaleno')
        else:
            linhas()
            print('O Triângulo não existe.')
    except ValueError:
        linhas()
        print('Erro! Insira somente valores numéricos.')