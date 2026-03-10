print("Saldão")

total_compra = float(input("Digite o valor do compra: "))
forma_pagamento = int(input("Digite o forma de pagamento: 1- Pix, 2- Cartão. "))

if forma_pagamento == 1:
    total_compra_desc = total_compra * 0.95
    print(f"o total da compra foi R${total_compra_desc: .2f}")
else:
    parcelas = int(input("informe o valor de parcelas desejadas: "))
    valor_parcela = total_compra / parcelas
    print(f"o total da compra foi R${total_compra:.2f} e valor de cada parcela é de R$: {valor_parcela:.2f}")