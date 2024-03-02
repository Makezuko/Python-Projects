nota_a = float(input('Insira o valor da nota no primeiro bimestre: '))
nota_b = float(input('Insira o valor da nota no segundo bimestre: '))
nota_c = float(input('Insira o valor da nota no terceiro bimestre: '))
nota_d = float(input('Insira o valor da nota no quarto bimestre: '))

media = (nota_a + nota_b + nota_c + nota_d)/2

print('A média foi de {:.2f}'.format(media))