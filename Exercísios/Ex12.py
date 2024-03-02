import random

ganho_por_hora = float(random.uniform(5, 300))
print('Ganho por hora: R${:.2f}'.format(ganho_por_hora))

horas_por_dia = float(random.randrange(1, 10))
print('Horas por dia: {}'.format(horas_por_dia))

dias_por_mes = float(random.randrange(1, 30))
print('Dias por mês: {}'.format(dias_por_mes))

horas_por_mês = horas_por_dia * dias_por_mes
print('Horas por mês: {}'.format(horas_por_mês))

salario_bruto = horas_por_mês * ganho_por_hora
print('Salário bruto: R${:.2f}'.format(salario_bruto))

inss = salario_bruto - (salario_bruto * 0.92)
print('Valor INSS: R${:.2f}'.format(inss))
sindicato = salario_bruto - (salario_bruto * 0.95)
print('Valor Sindicato: R${:.2f}'.format(sindicato))
imposto = salario_bruto - (salario_bruto * 0.89)
print('Valor Imposto de renda: R${:.2f}'.format(imposto))

salario_liquido = salario_bruto - inss - sindicato - imposto

print('Salário líquido: R${:.2f}'.format(salario_liquido))