from math import sqrt

print("Exercício 21: Números Primos\n")

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

inteiro = int(input("Por favor, digite um número inteiro qualquer: "))

if eh_primo(inteiro):
    print("Este número é primo.")
else:
    print("Este número não é primo.")