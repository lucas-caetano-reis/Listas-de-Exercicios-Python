print("Exercício 14: Pares e Ímpares\n")

numeros = []

while len(numeros) < 10:
    numero = int(input("Por favor, insira um número inteiro qualquer: "))
    numeros.append(numero)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nNúmeros pares ({len(pares)}): {pares}")
print(f"Números ímpares ({len(impares)}): {impares}")