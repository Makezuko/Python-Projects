carga_horaria = int(input('Insira quantas horas você trabalha ao dia: '))
dias_trabalho = int(input('Insira quantos dias ao mês você trabalha: '))
valor_hora = float(input('Insira o valor que você recebe por hora de trabalho: '))

calc = (valor_hora * carga_horaria) * dias_trabalho

print('O seu salário é de R${:.2f} ao mês'.format(calc))