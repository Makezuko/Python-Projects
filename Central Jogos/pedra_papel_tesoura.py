import random
import time

#Definir intervalos de tempo
def sleep(s):
        time.sleep(s)
#Definir linhas de separação
def linhas(l):
        print('='*l)
def escolha():
        int(input('O que você vai jogar? Pedra (1), Papel (2) ou Tesoura (3): '))
#Definir executavel para jogar
def jogar():
    #Gerando um número de 1 a 3
    rng = random.randrange(1, 4)

    sleep(0.8)

    linhas(80)

    escolha = int(input('O que você vai jogar? Pedra (1), Papel (2) ou Tesoura (3): '))

    linhas(80)

    sleep(0.85)
    #Caso o input seja um número inteiro diferente das opções, mensagem de erro em loop 
    while escolha != 1 and escolha != 2 and escolha != 3:
        print('Erro! Você precisa escrever uma das opções (1, 2 ou 3)')
        escolha = int(input('O que você vai jogar? Pedra (1), Papel (2) ou Tesoura (3): '))
        linhas(80)
        sleep(0.85)

    while escolha == rng:
        print('Empate! Tente novamente')
        rng = random.randrange(1, 4)
        linhas(80)
        escolha = int(input('O que você vai jogar? Pedra (1), Papel (2) ou Tesoura (3): '))
        linhas(80)
        sleep(0.85)
    
    if escolha == 1 and rng == 2:
        print('Você perdeu! Você escolheu Pedra e o computador Papel.')
        jogar_novamente()

    if escolha == 1 and rng == 3:
        print('Você Ganhou! Você escolheu Pedra e o computador Tesoura.')
        jogar_novamente()

    if escolha == 2 and rng == 3:
        print('Você perdeu! Você escolheu Papel e o computador Tesoura.')
        jogar_novamente()

    if escolha == 2 and rng == 1:
        print('Você Ganhou! Você escolheu Papel e o computador Pedra.')
        jogar_novamente()

    if escolha == 3 and rng == 1:
        print('Você perdeu! Você escolheu Tesoura e o computador Pedra.')
        jogar_novamente()

    if escolha == 3 and rng == 2:
        print('Você Ganhou! Você escolheu Tesoura e o computador Papel.')
        jogar_novamente()

#Escolha de continuar o jogo ou sair do aplicativo
def jogar_novamente():
    linhas(80)
    jogar_novamente = int(input('Quer jogar mais uma? Sim (1), Não (2): '))
    if jogar_novamente == 1:
        jogar()
    if jogar_novamente == 2:
        linhas(80)
        print('Até a próxima!')
        linhas(80)
        quit()
    while jogar_novamente != 1 or jogar_novamente != 2:
         linhas(80)
         print('Erro! Você precisa escrever uma das opções.')
         jogar_novamente()
