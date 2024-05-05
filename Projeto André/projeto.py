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

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: 
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
    if not agd:  
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
    if not agd: 
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
    if not agd:  
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
            print()  

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
