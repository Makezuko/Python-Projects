import random

c = 0

while c < 10:
    valor_horas = random.randrange(0, 24)
    valor_minutos = random.randrange(0, 60)
    valor_segundos = random.randrange(0, 60)
    str_horas = str(valor_horas).zfill(2)
    str_minutos = str(valor_minutos).zfill(2)
    str_segundos = str(valor_segundos).zfill(2)
    c = c + 1
    print('{}:{}:{}'.format(str_horas, str_minutos, str_segundos))