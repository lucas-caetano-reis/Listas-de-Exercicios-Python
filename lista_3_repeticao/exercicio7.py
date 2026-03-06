print("Exercício 7: Qual o Maior Número?\n")

numeros = []
while len(numeros) < 5:
    numero = float(input("Por favor, insira um número qualquer: "))
    numeros.append(numero)

maior = float('-inf')
for numero in numeros:
    if numero > maior:
        maior = numero

print(f"Maior número: {numero}")