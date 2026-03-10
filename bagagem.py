tipo_cliente = input("informe o tipo de cliente: PREMIUM, GOLD ou REGULAR: ")
peso_bagagem = float(input("informe o valor do peso do bagagem: "))

if tipo_cliente == "PREMIUM":
    #verificacao peso bagagem premium
    if peso_bagagem <= 32:
        print("pode levar a bagagem")
    #peso excedente
    else:
        peso_excedente = peso_bagagem - 32
        print(f"peso excedente é de {peso_excedente:.2f} kg")
#GOLD
elif tipo_cliente == "GOLD":
    #verificacao peso bagagem gold
    if peso_bagagem <= 28:
        print("pode levar a bagagem")
    else:
        #peso excedente
        peso_excedente = peso_bagagem - 28
        print(f"peso excedente é de {peso_excedente:.2f} kg")
    #REGULAR
else:
    #verificacao peso bagagem regular
    if tipo_cliente == "REGULAR":
        print("é necessário ir ao balcão pagar a mala")
