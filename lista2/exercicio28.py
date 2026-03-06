import sys

print("Exercício 28: Hipermercado Tabajara")

tipo_carne = str(input("\nPor favor, insira o tipo de carne a ser comprada - File Duplo, Alcatra ou Picanha: "))

if tipo_carne != "File Duplo" and tipo_carne != "Alcatra" and tipo_carne != "Picanha":
    print("\nOpção inválida. Por favor, tente novamente.")
    sys.exit()

quantidade = int(input("\nPor favor, insira a quantidade de carne a ser comprada: "))

if tipo_carne == "File Duplo":
    if quantidade <= 5:
        preco = quantidade * 4.9
    else:
        preco = quantidade * 5.8

if tipo_carne == "Alcatra":
    if quantidade <= 5:
        preco = quantidade * 5.9
    else:
        preco = quantidade * 6.8

if tipo_carne == "Picanha":
    if quantidade <= 5:
        preco = quantidade * 6.9
    else:
        preco = quantidade * 7.8

tipo_pagamento = str(input("\nPor favor, insira o tipo de pagamento - Dinheiro ou Cartão Tabajara: "))
desconto = 0

if tipo_pagamento == "Dinheiro":
    preco_final = preco

elif tipo_pagamento == "Cartão Tabajara":
    desconto = 0.05
    preco_final = preco - preco * desconto

else:
    print("\nOpção inválida. Por favor, tente novamente.")
    sys.exit()

print("\nCupom Fiscal:\n")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade}")
print(f"Valor da compra: {preco:.2f}")
print(f"Forma de pagamento: {tipo_pagamento}")
print(f"Desconto: {desconto}")
print(f"Valor final: {preco_final:.2f}")