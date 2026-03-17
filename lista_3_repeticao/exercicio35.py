from math import sqrt

print("Exercício 35: Todos os números primos entre 1 e N\n")

def crivo_eratostenes(num):
    numeros = [True] * (num + 1)
    numeros[0] = numeros[1] = False

    for i in range(2, int(sqrt(num)) + 1):
        for j in range(i * i, num + 1, i):
                if numeros[j]:
                    numeros[j] = False

    primos = []
    for i in range(2, num + 1):
        if numeros[i]:
            primos.append(i)

    return primos

numero = int(input("Digite um número inteiro qualquer: "))
while numero <= 1:
    print("\nO número deve ser maior que 1!\n")
    numero = int(input("Digite um número inteiro qualquer: "))

primos = crivo_eratostenes(numero)

print(f"Lista de números primos entre 1 e {numero}: {primos}")