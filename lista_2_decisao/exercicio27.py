print("Exercício 27: Fruteira")

morangos = int(input("Por favor, insira a quantidade de morangos (em kg): "))
macas = int(input("Por favor, insira a quantidade maças (em kg): "))

if morangos <= 5:
    preco_morangos = morangos * 2.5
else:
    preco_morangos = morangos * 2.2

if macas <= 5:
    preco_macas = macas * 1.8
else:
    preco_macas = macas * 1.5

preco_total = preco_morangos + preco_macas

if morangos + macas > 8 or preco_total > 25:
    preco_final = preco_total - preco_total * 0.10

print(f"Preço total da compra: {preco_final}")