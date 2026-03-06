print("Exercício 1: Qual o maior número?")

numero1 = float(input("Digite um número qualquer: "))
numero2 = float(input("Digite um segundo número: "))

if numero1 > numero2:
    print(f"Maior número: {numero1}")
elif numero2 > numero1:
    print(f"Maior número: {numero2}")
else:
    print(f"Os dois números são iguais.")