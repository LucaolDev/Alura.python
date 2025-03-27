import os

restaurantes = [{"nome": "Son sushi", "categoria": "Japonesa", "ativo": False},
                {"nome": "Pizza Suprema", "categoria": "Italiana", "ativo": True},
                {"nome": "Dubai", "categoria": "Armênio", "ativo": False}
                ]


def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def exibir_opcoes():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")


def finalizar_app():
    exibir_subtitulo("Finalizar o app")


def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu: ")
    main()


def opcao_invalida():
    print("Opção invalida!\n")
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    exibir_subtitulo("Cadastrando o restaurante")
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite o categoria do restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome": nome_do_restaurante, "categoria": categoria, "ativo": False}
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")
    restaurantes.append(dados_do_restaurante)
    voltar_ao_menu_principal()


def listar_restaurantes():
    exibir_subtitulo("Listando os restaurantes")

    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        aivo = restaurante["ativo"]
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {aivo}")

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    exibir_subtitulo("Alterando o restaurante")
    nome_restaurante = input("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso!" if restaurante[
                "ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso! "
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

    voltar_ao_menu_principal()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print("\n")
        # print(f"Você escolheu a opção: {opcao_escolhida}")

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == "__main__":
    main()
