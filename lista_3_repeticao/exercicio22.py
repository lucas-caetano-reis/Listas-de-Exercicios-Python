from math import sqrt

print("Exercício 22: Divisores de um número primo\n")

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def encontrar_divisores(num):
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

inteiro = int(input("Por favor, digite um número inteiro qualquer: "))

if eh_primo(inteiro):
    print("Este número é primo.")
else:
    print("Este número não é primo.")
    print(f"Divisores de {inteiro}: {encontrar_divisores(inteiro)}")