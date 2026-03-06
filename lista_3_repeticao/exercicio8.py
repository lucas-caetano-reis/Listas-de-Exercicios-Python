print("Exercício 8: Soma e Média de 5 Números\n")

numeros = []
while len(numeros) < 5:
    numero = float(input("Por favor, insira um número qualquer: "))
    numeros.append(numero)

soma = 0

for numero in numeros:
    soma += numero

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media}")