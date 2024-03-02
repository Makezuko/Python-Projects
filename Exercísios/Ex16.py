sexo = str(input('Insira se você é do sexo masculino(M), feminino(F) ou outro(O): '))

sexo = sexo.capitalize()

if sexo == ('M'):
    print('Você escolheu o sexo masculino')
if sexo == ('F'):
    print('Você escolheu o sexo feminino')
if sexo  == ('O'):
    print('Você escolheu um outro tipo de gênero.')
    str(input('Por favor insira o gênero que você se identifica: '))
else:
    print('Erro! Não foi possível identificar o gênero inserido, por favor tente novamente.')