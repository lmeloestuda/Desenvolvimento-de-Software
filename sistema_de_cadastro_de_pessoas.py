def criar_usuario(lista_usuarios, proximo_id):
    """
    Cria um novo usuário e adiciona à lista.

    lista_usuarios: list
    proximo_id: int
    retorno: int (novo proximo_id)
    """

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    usuario = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade
    }

    list.append(lista_usuarios, usuario)

    print("Usuário criado com sucesso.")

    return proximo_id + 1


def listar_usuarios(lista_usuarios):
    """
    Lista todos os usuários cadastrados.

    lista_usuarios: list
    retorno: None
    """

    if len(lista_usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in lista_usuarios:
            print("ID:", usuario["id"])
            print("Nome:", usuario["nome"])
            print("Idade:", usuario["idade"])
            print("-------------------")


def atualizar_usuario(lista_usuarios):
    """
    Atualiza os dados de um usuário.

    lista_usuarios: list
    retorno: None
    """

    id_busca = int(input("Digite o ID do usuário: "))

    for usuario in lista_usuarios:
        if usuario["id"] == id_busca:

            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))

            usuario["nome"] = novo_nome
            usuario["idade"] = nova_idade

            print("Usuário atualizado com sucesso.")
            return

    print("Usuário não encontrado.")


def remover_usuario(lista_usuarios):
    """
    Remove um usuário da lista.

    lista_usuarios: list
    retorno: None
    """

    id_busca = int(input("Digite o ID do usuário: "))

    for usuario in lista_usuarios:
        if usuario["id"] == id_busca:
            list.remove(lista_usuarios, usuario)
            print("Usuário removido com sucesso.")
            return

    print("Usuário não encontrado.")


def sistema():
    """
    Função principal do sistema CRUD.

    retorno: None
    """

    usuarios = []
    proximo_id = 1

    continuar = True

    while continuar:

        print("\n=== SISTEMA CRUD ===")
        print("1 - Criar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Remover usuário")
        print("0 - Sair")

        opcao = input("Digite a opção: ")

        if opcao == "1":
            proximo_id = criar_usuario(usuarios, proximo_id)

        elif opcao == "2":
            listar_usuarios(usuarios)

        elif opcao == "3":
            atualizar_usuario(usuarios)

        elif opcao == "4":
            remover_usuario(usuarios)

        elif opcao == "0":
            continuar = False

        else:
            print("Opção inválida.")


sistema()
