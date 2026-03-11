op = 0
ficha = {}

while op != 4:
    print("Ficha Cadastral")
    print("1 - Incluir informações na ficha")
    print("2 - Recuperar informações na ficha")
    print("3 - Exibir a ficha completa")
    print("4 - Sair")
    op = int(input("Digite sua opcao: "))

    if op == 1:
        chave = input("Informe o nome que deseja cadastrar: ")
        valor = input("Informe o dado que deseja cadastrar: ")
        #ficha[chave] = valor
        ficha.update({chave: valor})
    elif op == 2:
        print(f"os campos disponiveis são {ficha.keys}")
        chave = input("Informe o campo que deseja exibir: ")

        if chave in ficha.keys():
            print(f"{ficha[chave]}")
        else:
            print("Opcao invalida")
    elif op == 3:
        print("ficha cadastral")
        for campo, dado in ficha.items():
            print(f"{campo} - {dado}")
    elif op == 4:
        print("Saindo do sistema")
        break
    else:
        print("Opcao invalida")