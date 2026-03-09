print("Cadastro de doadores de sangue")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso: "))
altura = int(input("Digite sua altura em cm: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = 2026 - ano_nascimento

peso_minimo = peso > 50
idade_minima = ano_nascimento > 18

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso} kg \n\tALTURA: {altura} cm\n\tIDADE: {idade}"

print(texto_saida)