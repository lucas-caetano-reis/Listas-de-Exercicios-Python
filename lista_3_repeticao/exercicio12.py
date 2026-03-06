print("Exercício 12: Gerador de Tabuada\n")

numero = int(input("Por favor, insira um número inteiro entre 1 e 10: "))
while numero < 1 or numero > 10:
    numero = int(input("Por favor, insira um número inteiro entre 1 e 10: "))

print(f"\nTabuada de {numero}:")
for grau in range(1, 11):
    print(f"{numero} X {grau}: = {numero * grau}")