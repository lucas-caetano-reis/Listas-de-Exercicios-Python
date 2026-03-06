print("Exercício 9: Ordenar números em ordem decrescente")

numero1 = float(input("Digite um número qualquer: "))
numero2 = float(input("Digite um segundo número: "))
numero3 = float(input("Digite um terceiro número: "))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

print(f"Lista ordenada em ordem decrescente: {numeros}")