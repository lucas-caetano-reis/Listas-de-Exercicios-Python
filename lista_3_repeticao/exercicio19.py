print("Exercício 19: Menor valor, maior valor e soma de valores entre 0 e 1000\n")

n = int(input("Por favor, insira o número de itens que serão contidos no conjunto: "))
conjunto = []

maior = float('-inf')
menor = float('inf')
soma = 0

for i in range(n):
    conjunto.append(float(input(f"Por favor, insira o {i + 1}° item do conjunto: ")))
    while conjunto[i] < 0 or conjunto[i] > 1000:
        print("Valor inválido. O item deve estar entre 0 e 1000.\n")
        conjunto[i] = float(input(f"Por favor, insira o {i + 1}° item do conjunto: "))

    if conjunto[i] > maior:
        maior = conjunto[i]
    if conjunto[i] < menor:
        menor = conjunto[i]

    soma += conjunto[i]

print(f"\nConjunto: {conjunto}")
print(f"Maior valor do conjunto: {maior}")
print(f"Menor valor do conjunto: {menor}")
print(f"Soma dos valores do conjunto: {soma}")