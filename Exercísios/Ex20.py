# Is x Divisible by n?
x = int(input('Insira o valor a ser dividido: '))
n = int(input('Insira o valor do divisor: '))

if x % n == 0:
    print('O valor {} pode ser dividido pelo número {}'.format(x, n))
    print('A divisão resulta em {}'.format(float(x/n)))
if x % n != 0:
    print('O valor {} não pode ser dividido exatamente pelo número {}'.format(x, n))
    print('A divisão resulta em {}'.format(float(x/n)))