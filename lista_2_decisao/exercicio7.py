print("Exercício 7: Maior e menor número")

numero1 = float(input("Digite um número qualquer: "))
numero2 = float(input("Digite um segundo número: "))
numero3 = float(input("Digite um terceiro número: "))

numeros = [numero1, numero2, numero3]

maior = float('-inf')
menor = float('inf')

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")