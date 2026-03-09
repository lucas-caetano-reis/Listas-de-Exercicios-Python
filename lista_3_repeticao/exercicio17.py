print("Exercício 17: Fatorial de um número inteiro\n")

inteiro = int(input("Por favor, insira um número inteiro qualquer: "))
fatorial = inteiro

for i in range(inteiro - 1, 0, -1):
    fatorial *= i

print(f"Fatorial de {inteiro}: {fatorial}")