print("Exercício 32: Fatorial de um número\n")

def calcular_fatorial(num):
    fatores = []
    fatores.append(num)

    fatorial = num

    for i in range(num - 1, 0, -1):
        fatores.append(i)
        fatorial *= i

    return fatorial, fatores

numero = int(input("Digite um número inteiro qualquer: "))
while numero <= 0:
    print("\nO número não pode ser menor ou igual a zero!\n")
    numero = int(input("Digite um número inteiro qualquer: "))

fatorial, fatores = calcular_fatorial(numero)

print(f"Fatorial de {numero}: {numero}! = {fatores} = {fatorial}")