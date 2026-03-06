print("Exercício 6: de 1 a 20\n")

numeros = 0

print("Mostrando os número de 1 a 20 na vertical:")
while numeros < 20:
    numeros += 1
    print(numeros)

numeros = []
i = 0

print("\nMostrando os número de 1 a 20 na horizontal:")
while len(numeros) < 20:
    i += 1
    numeros.append(i)

print(numeros)