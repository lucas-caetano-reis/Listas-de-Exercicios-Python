print("Exercício 9: Todos os números ímpares entre 1 e 50\n")

impares = []


for numero in range(1, 51):
    if numero % 2 != 0:
        impares.append(numero)

print(f"Números ímpares de 1 a 50: {impares}")