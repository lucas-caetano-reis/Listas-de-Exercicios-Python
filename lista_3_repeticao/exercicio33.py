print("Exercício 33: Temperaturas\n")

maior = float('-inf')
menor = float('inf')

tamanho = int(input("Informe o tamanho do conjunto de temperaturas: "))
while tamanho <= 0:
    print("\nO conjunto deve conter ao menos uma temperatura!\n")
    tamanho = int(input("Informe o tamanho do conjunto de temperaturas: "))

conjunto = []
soma = 0

for i in range(0, tamanho):
    conjunto.append(float(input(f"Temperatura {i + 1}: ")))

    if conjunto[i] > maior:
        maior = conjunto[i]
    if conjunto[i] < menor:
        menor = conjunto[i]

    soma += conjunto[i]

media = soma / tamanho

print(f"\nMaior temperatura: {maior}")
print(f"Menor temperatura: {menor}")
print(f"Média das temperaturas: {media}")