opcao = 0

while opcao != 3:
    print("1 - Receber um elogio")
    print("2 - Calcular fatorial")
    print("3 - Sair")
    opcao = int(input("informe a opcao: "))

    if opcao == 1:
        print("gato rs\n")
    elif opcao == 2:
        #fatorial
        numero = int(int(input("informe um numero inteiro: ")))
        fat = numero

        for valor in range(1, numero, 1):
            fat = fat * valor
        print(f"o resultado é: {fat}\n")
    elif opcao == 3:
        print("saindo do menu")
    else:
        print("escolha opcao valida!")