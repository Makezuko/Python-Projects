def programa():
    try:
        peso = float(input('Insira o peso em kg: '))
        altura = float(input('Insira a altura em M: '))
        while peso <= 0 or altura <= 0:
            print('Erro! Os valores precisam ser positivos')
            programa()
        imc = peso / altura**2
        print('O IMC de uma pessoa com {:.2f}kg e {:.2f}M é de {:.2f}'.format(peso, altura, imc))
        if imc < 18.5:
            print('O IMC indica que a pessoa está abaixo do peso.')
        if imc >= 18.5 and imc < 25:
            print('O IMC indica que a pessoa está com o peso normal.')
        if imc >= 25 and imc < 30:
            print('O IMC indica que a pessoa está abaixo com sobrepeso.')
        if imc >= 30 and imc < 35:
            print('O IMC indica que a pessoa está com obesidade classe 1.')
        if imc > 35 and imc < 40:
            print('O IMC indica que a pessoa está com obesidade classe 2 (Severa).')
        if imc > 40:
            print('O IMC indica que a pessoa está com obesidade classe 3 (Mórbida)')
    except ValueError:
        print('Erro! Os valores inseridos precisam ser numéricos.')
print('Bem-vindo ao programa que calcula o Indice de Massa Corporal.')
programa()