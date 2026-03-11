calorias = []
resposta = ""

while resposta.upper() != "NÃO":
    caloria = int(input("Quantas calorias nessa refeição? "))
    calorias.append(caloria)
    resposta = input("você deseja informar as calorias de mais uma refeição? ")

total = 0
for caloria in calorias:
    print(f"nesta refeirção foram consumidas {caloria} calorias")
    total = total + caloria

media = total / len(calorias)
print(f"neste dia a media consumida foi de {media:.2f} calorias")