import time
#Importar executáveis de outro arquivo
from pedra_papel_tesoura import jogar
from pedra_papel_tesoura import jogar_novamente

#Definir intervalos de tempo
def sleep(s):
        time.sleep(s)
#Definir linhas de separação
def linhas(l):
        print('='*l)
#Definir escolha de jogo
def game_choice():
        game_id = int(input('Pedra, papel ou tesoura (1): '))

        while game_id != 1:
                print('Erro! Você precisa escrever uma das opções (1)')
                game_id = int(input('Pedra, papel ou tesoura (1): '))
                

        if game_id== 1:
                jogar()


linhas(80)

print('Seja bem-vinda/o à central de jogos!')
print('O que você quer jogar?')

#Execução da escolha feita
game_choice()

