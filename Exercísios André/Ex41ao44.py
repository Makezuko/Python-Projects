unidades = ['', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
especiais = ['dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezenas = ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centenas = ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

def numero_por_extenso(numero):
    extenso = ''

    if numero < 0:
        extenso += 'menos '
        numero = abs(numero)

    if numero == 0:
        return 'zero'

    if numero >= 100:
        extenso += centenas[numero // 100]
        numero %= 100
        if numero > 0:
            extenso += ' e '

    if numero >= 20:
        extenso += dezenas[numero // 10]
        numero %= 10
        if numero > 0:
            extenso += ' e '

    if numero >= 10:
        extenso += especiais[numero - 10]
    elif numero > 0:
        extenso += unidades[numero]

    return extenso

while True:
    try:
        numero = int(input("Digite um número entre -999 e 999: "))
        if -999 <= numero <= 999:
            print("O número por extenso é:", numero_por_extenso(numero))
            break
        else:
            print("Número fora do intervalo permitido!")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")