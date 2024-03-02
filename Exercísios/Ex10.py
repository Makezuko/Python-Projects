import time

def linhas():
    print('-'*60)

def init():
    
    linhas()
    print('Bem-vindo à calculadora de peso ideal')
    linhas()
    time.sleep(0.8)
    calculadora()
    linhas()
    time.sleep(1)

def calculadora():
    gênero = int(input('O indivíduo é de que gênero? Masculino(1), Feminino(2): '))
    while gênero != 1 and gênero != 2:
        print('Erro! Você precisa inserir um dos valores apresentados.')
        gênero = int(input('O indivíduo é de que gênero? Masculino(1), Feminino(2): '))
    altura = float(input('Insira a altura: '))
    linhas()
    if  gênero == 1:
        peso_ideal = (72.7 * altura) - 58
        print('O peso ideal para uma pessoa do sexo masculino com {:.2f}m de altura é de aproximadamente {:.2f}kg'.format(altura, peso_ideal))
    if gênero == 2:
        peso_ideal = (62.1 * altura) - 44.7
        print('O peso ideal para uma pessoa do sexo feminino com {:.2f}m de altura é de aproximadamente {:.2f}kg'.format(altura, peso_ideal))

init()

