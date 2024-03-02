#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
#Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Insira o peso do peixe em quilos: '))
while peso == 0:
    print('Erro! A balança não está registrando peso!')
    peso = float(input('Insira o peso do peixe em quilos: '))
while peso < 0:
    print('Erro! O peso não pode ser um valor negativo.')
    peso = float(input('Insira o peso do peixe em quilos: '))
if peso > 50:
    peso_excedente = (peso - 50)
    multa = peso_excedente * 4.00
    print('O peixe tem um peso excedente de {:.2f}kg'.format(peso_excedente))
    print('Com a taxa estabelecida de R$4.00 por quilo, a multa será de R${:.2f}'.format(multa))
if peso <= 50 and peso > 0:
    print('O peso esta dentro do regulamento de pesca estabelecido pelo governo de São Paulo')