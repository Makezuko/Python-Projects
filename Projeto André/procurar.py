# Implementar a opção 2 (procurar contato) da seguinte forma:
# Ficar pedindo para digitar um nome até digitar um nome que existe;
# mostrar então na tela TODOS os demais dados daquela pessoa, cujo
# nome foi digitado.

# Implementar a opção 3 (atualizar contato) da seguinte forma:
# Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
# endereco, ou telefone, ou celular, ou email, ou finalizar as
# atualizações; ficar pedindo para digitar a opção até digitar uma
# opção válida; realizar a atulização solicitada; até ser escolhida a
# opção de finalizar as atualizações.

# Implementar a opção 4 (listar contato) da seguinte forma:
# Mostrar na tela os TODOS os dados de CADA um dos contatos presentes
# na lista chamada agenda (eventualmente chamada de agd).

# Entregar até domingo, dia 28 de abril de 2024.
# '''

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Matias Amma (24000419)                                      |')
    print('| Kauê Farias (24788788)                                      |')
    print('| Rafael Zorzetto (22008059)                                  |')
    print('|                                                             |')
    print('| Versão 2.0 de 12/abril/2024                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

# '''
# procura nom em agd e, se achou, retorna:
# uma lista contendo True e a posicao onde achou;
# MAS, se não achou, retorna:
# uma lista contendo False e a posição onde inserir,
# aquilo que foi buscado, mas nao foi encontrado,
# mantendo a ordenação da lista.
# '''

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar(agd):
    if not agd:  # Verifica se a agenda está vazia
        print('Não há contatos cadastrados.')
    else: 
        for contato in agenda:
            print(contato)
        while True:
            alvo = input('Insira o nome do contato (digite "sair" para voltar ao menu): ')
            if alvo.lower() == "sair":
                break
            else:
                encontrado = False
                primeiro = 0
                ultimo = len(agd) - 1
                while primeiro <= ultimo:
                    meio = (primeiro + ultimo) // 2
                    if agd[meio][0].lower() == alvo.lower():
                        print('Nome.......:', agd[meio][0])
                        print('Aniversário:', agd[meio][1])
                        print('Endereço...:', agd[meio][2])
                        print('Telefone...:', agd[meio][3])
                        print('Celular....:', agd[meio][4])
                        print('e-mail.....:', agd[meio][5])
                        encontrado = True
                        break
                    elif agd[meio][0].lower() < alvo.lower():
                        primeiro = meio + 1
                    else:
                        ultimo = meio - 1
                if not encontrado:
                    print('Contato não encontrado')

def menuAtualizar():
    menuAtualizar = [
        "Aniversário",\
        "Endereço",\
        "Telefone",\
        "Celular",\
        "e-mail"]
    opcoesValidas=[]
    posicao=0
    while posicao<len(menuAtualizar):
        print (posicao+1,') ',menuAtualizar[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1  

def atualizar(agd):
    if not agd:  # Verifica se a agenda está vazia
        print('Não há contatos cadastrados.')
    else:
        while True:
            encontrado = False
            alvo = input('Insira o nome do contato a ser atualizado (digite "sair" para voltar ao menu): ')
            if alvo.lower() == "sair":
                break
            else:
                primeiro = 0
                ultimo = len(agd) - 1
                while primeiro <= ultimo:
                    meio = (primeiro + ultimo) // 2
                    if agd[meio][0].lower() == alvo.lower():
                        encontrado = True
                        break
                    elif agd[meio][0].lower() < alvo.lower():
                        primeiro = meio + 1
                    else:
                        ultimo = meio - 1
                if not encontrado:
                    print('Contato não encontrado')
                    continue

            menuAtualizar()
            inputAtualizar = input('O que você deseja atualizar? (digite "sair" para voltar): ')
            if inputAtualizar.lower() == "sair":
                break
            inputAtualizar = int(inputAtualizar)
            novo_valor = input('Digite o novo valor: ')
            agd[meio][inputAtualizar] = novo_valor
            print('Contato atualizado com sucesso!')

            

def listar(agd):
    if not agd:  # Verifica se a agenda está vazia
        print('Não há contatos cadastrados.')
    else:
        print('Listagem de Contatos:')
        for contato in agd:
            print('Nome:', contato[0])
            print('Aniversário:', contato[1])
            print('Endereço:', contato[2])
            print('Telefone:', contato[3])
            print('Celular:', contato[4])
            print('E-mail:', contato[5])
            print()  # Adiciona uma linha em branco entre os contatos

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

opcao=666
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
