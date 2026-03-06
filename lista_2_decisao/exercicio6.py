print("Exercício 6: Qual o maior número?")

numero1 = float(input("Digite um número qualquer: "))
numero2 = float(input("Digite um segundo número: "))
numero3 = float(input("Digite um terceiro número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"Maior número: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"Maior número: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"Maior número: {numero3}")
else:
    print(f"Os três números são iguais")