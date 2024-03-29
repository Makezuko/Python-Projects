def numero_extenso():
    unidades = {
        0 : 'zero', 1: 'um', 2 : 'dois', 3 : 'três', 4 : 'quatro',
        5 : 'cinco', 6 : 'seis', 7 : 'sete', 8 : 'oito', 9 : 'nove'
    }

    especiais = {
        10 : 'dez', 11: 'onze', 12 : 'doze', 13 : 'treze', 14 : 'quatorze', 15 : 'quinze',
        16 : 'dezesseis', 17 : 'dezessete', 18 : 'dezoito', 19 : 'dezenove', 100: 'cem'
    }

    dezenas = {
        2 : 'vinte', 3 : 'trinta', 4 : 'quarenta', 5 : 'cinquenta',
        6 : 'sessenta', 7 : 'setenta', 8 : 'oitenta', 9 : 'noventa'
    }

    centenas = {
        1: 'cento', 2 : 'duzentos', 3 : 'trezentos', 4 : 'quatrocentos',
        5 : 'quinhentos', 6 : 'seiscentos', 7 : 'setecentos', 8 : 'oitocentos', 9 : 'novecentos'
    }
    
    while True:
        try:
            num = int(input("Digite um número entre -999 e 999: "))
            if -999 <= num <= 999:
                break
            else:
                print("Número fora dos limites permitidos.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    if num == 0:
        return unidades[num]

    if num < 0:
        extenso = 'menos '
        num = abs(num)
    else:
        extenso = ''
    centena = num//100
    dezena = (num%100)//10
    unidade = num%10
    if centena != 0:
        if centena == 1 and dezena == 0 and unidade == 0:  
            extenso += especiais[100]
        else:
            extenso += centenas[centena]
            if dezena == 0 and unidade == 0:
                return extenso
            else:
                extenso += ' e '
    if dezena == 1:
        extenso += especiais[num%100]
    else: 
        if dezena != 0:
            extenso += dezenas[dezena]
            if unidade != 0:
                extenso += ' e '
        if unidade != 0:
            extenso += unidades[unidade]  
    return extenso

print(numero_extenso())