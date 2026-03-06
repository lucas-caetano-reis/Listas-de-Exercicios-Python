print("Exercício 8: Produto mais barato")

preco1 = float(input("Digite o preço de um produto qualquer: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

precos = [preco1, preco2, preco3]

mais_barato = float('inf')

for preco in precos:
    if preco < mais_barato:
        mais_barato = preco

print(f"Você deve comprar o produto cujo preço é {mais_barato}")