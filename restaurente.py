preco_quilo = float(input("Informe o valor cobrado por quilo: "))
peso_prato = float(input("Informe o peso do prato em KG: "))

preco_prato = preco_quilo * peso_prato

print(f"o valor do prato em R${preco_prato:.2f}")

if peso_prato > 1:
    print("como o peso passou de 1kg, o valor será de 70R$")