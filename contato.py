def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        '''
        nome/email/telefone
        '''
        arquivo.write(
            f"{contato['nome']}#{contato['email']}#{contato['tel']}\n")

    arquivo.close()


def carregar_contatos():
    lista = []

    try:
        arquivo = open("contatos.txt", "r")

        for linha in arquivo.readlines():
            coluna = linha.strip().split("#")

            contato = {
                "email": coluna[1],
                "nome": coluna[0],
                "tel": coluna[2],
            }

            lista.append(contato)

        arquivo.close()
    except FileNotFoundError:
        pass

    return lista


def existe_contato(lista, email):

    if len(lista) > 0:
        for contato in lista:
            if contato['email'] == email:
                return True

    return False


def adicionar(lista):

    while True:
        email = input("Digite o e-mail do contato: ")

        if not existe_contato(lista, email):
            break
        else:
            print("Esse e-mail já foi utilizado.")
            print("Por favor tente um novo e-mail.")

        # Nesse passo, o e-mail recido será único

    contato = {
        "email": email,
        "nome": input("Digite o nome: "),
        "tel": input("Digite o telefone: "),
    }

    lista.append(contato)

    print(f"O contato {contato['nome']} foi cadastrado com sucesso")


def alterar(lista):
    print("== Alterar Contato ==")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser Alterado: ")
        if existe_contato(lista, email):
            print("O contato foi encontardo. As informações seguem abaixo:")
            for contato in lista:
                if contato['email'] == email:
                    print(f"Nome: {contato['nome']}")
                    print(f"Email: {contato['email']}")
                    print(f"Telefone: {contato['tel']}")
                    print("=" * 20)
                    print("\n")

                    contato['nome'] = input("Digite o novo nome do contato: ")
                    contato['tel'] = input(
                        "Digite o novo telefone do contato:  ")

                    print(
                        f"Os dados do contato {contato['email']}, foram alterado com secesso!")

                    break

        else:
            print(
                f"Não existe contato cadastrado no sistema com esse e-mail {email}. \n ")
    else:
        print("Não existe nenhum cadastrado no sistema")


def excluir(lista):
    print("== Excluir Contatos ==")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser excluído: ")
        if existe_contato(lista, email):
            print("O contato foi encontardo. As informações seguem abaixo:")
            for i, contato in enumerate(lista):
                if contato['email'] == email:
                    print(f"Nome: {contato['nome']}")
                    print(f"Email: {contato['email']}")
                    print(f"Telefone: {contato['tel']}")
                    print("=" * 20)
                    print("\n")

                    del lista[i]

                    print("O contato foi apagado com sucesso! \n")
                    break

        else:
            print(
                f"Não existe contato cadastrado no sistema com esse e-mail {email}. \n ")
    else:
        print("Não existe nenhum cadastrado no sistema")


def buscar(lista):
    print("== Buscar Contato ==")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser encontrado: ")
        if existe_contato(lista, email):
            print("O contato foi encontardo. As informações seguem abaixo:")
            for contato in lista:
                if contato['email'] == email:
                    print(f"Nome: {contato['nome']}")
                    print(f"Email: {contato['email']}")
                    print(f"Telefone: {contato['tel']}")
                    print("=" * 20)
                    print("\n")
                    break

        else:
            print(
                f"Não existe contato cadastrado no sistema com esse e-mail {email}. \n ")
    else:
        print("Não existe nenhum cadastrado no sistema")


def listar(lista):
    print("== Lista Contatos ==")
    if len(lista) > 0:
        for i, contato in enumerate(lista):
            print(f"Contato {i+1}")
            print(f"\tNome: {contato['nome']}")
            print(f"\tEmail: {contato['email']}")
            print(f"\tTelefone: {contato['tel']}")
            print("=" * 40)
        print(f"Quantidade de Contatos: {len(lista)}")
    else:
        print("Não existe nenhum cadastrado no sistema")


def principal():

    lista = carregar_contatos()  # Inicializando a lista de contatos

    while True:
        print("=== Agenda telefônica ===")
        print(" 1 - Adicionar contato")
        print(" 2 - Alterar contato")
        print(" 3 - Excluir contato")
        print(" 4 - Buscar contato")
        print(" 5 - Listar contato")
        print(" 6 - Sair")
        opcao = int(input("> "))

        if opcao == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opcao == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opcao == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print("Finalizando...")
            break
        else:
            print("Dados inválidos. Por favor, tente novamente.")


principal()
