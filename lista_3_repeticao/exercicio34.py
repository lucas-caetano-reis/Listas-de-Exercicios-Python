from math import sqrt

print("Exercício 34: É ou não é primo?")

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro qualquer: "))

if eh_primo(numero):
    print("Este número é primo.")
else:
    print("Este número não é primo.")