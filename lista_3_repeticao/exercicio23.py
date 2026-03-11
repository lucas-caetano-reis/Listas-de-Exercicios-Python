from math import sqrt

print("Exercício 23: Todos os números primos entre 1 e N\n")

def crivo_eratostenes(num):
    numeros = [True] * (num + 1)
    numeros[0] = numeros[1] = False

    eliminacoes = 0

    for i in range(2, int(sqrt(num)) + 1):
        for j in range(i * i, num + 1, i):
                if numeros[j]:
                    numeros[j] = False
                    eliminacoes += 1

    primos = []
    for i in range(2, num + 1):
        if numeros[i]:
            primos.append(i)

    return primos, eliminacoes

"""
def eh_primo(num):
    divisoes = 0

    if num < 2:
        return False, divisoes
    
    for i in range(2, int(sqrt(num)) + 1):
        divisoes += 1
        if num % i == 0:
            return False, divisoes
        
    return True, divisoes

def encontrar_primos(num):
    primos = []
    total_divisoes = 0

    for i in range(1, num + 1):
        primo, divisoes = eh_primo(i)
        total_divisoes += divisoes
        
        if primo:
            primos.append(i)

    return primos, total_divisoes
"""

n = int(input("Por favor, digite um número inteiro maior que 1: "))
while n <= 1:
    n = int(input("Por favor, digite um número inteiro maior que 1: "))

primos, eliminacoes = crivo_eratostenes(n)

print(f"Números primos entre 1 e {n}: {primos}")
print(f"Número de eliminacoes realizadas pelo crivo: {eliminacoes}")