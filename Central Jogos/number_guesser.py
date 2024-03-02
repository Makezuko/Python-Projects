import random
import time

dificuldade = ''

def jogar_number_guesser():
    print('Bem-vindo ao Number Guesser!')
    d = int(input('Insira a dificuldade desejada Fácil(1), Média(2) ou Difícil(3): '))
    if d == 1:
        dificuldade = 'Fácil'
        print('Você escolheu a dificuldade {}'.format(dificuldade))
        tentativas + 5
    if d == 2:
        dificuldade = 'Média'
        print('Você escolheu a dificuldade {}'.format(dificuldade)) 
        tentativas + 3
    if d == 3:
        dificuldade = 'Difícil'
        print('Você escolheu a dificuldade {}'.format(dificuldade))
        tentativas + 2
    while d != 1 and d != 2 and d != 3:
            print('Erro! Você precisa inserir uma das opções.')
            d = int(input('Insira a dificuldade desejada Fácil(1), Média(2) ou Difícil(3): '))

    x = int(random.randrange(0, 11))

    chute = int(input('Chute um número de 1 a 10!: '))

    if chute != x:
        tentativas = tentativas - 1
        print(tentativas)
        if tentativas == 0:
            print('Acabaram as tentativas')
    if chute == x:
         print('Você acertou!')

jogar_number_guesser()