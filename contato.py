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


def alterar():
    pass


def excluir():
    pass


def buscar():
    pass


def listar():
    pass


def principal():

    lista = []  # Inicializando a lista vazia

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
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            buscar()
        elif opcao == 5:
            listar()
        elif opcao == 6:
            print("Finalizando...")
            break
        else:
            print("Dados inválidos. Por favor, tente novamente.")


principal()
