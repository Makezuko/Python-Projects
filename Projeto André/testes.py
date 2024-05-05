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

listar()