print("Exercício 24: Média Aritmética de N Notas\n")

n = int(input("Por favor, digite o número de notas a serem analisadas: "))
while n <= 0:
    print("\nDeve haver pelo menos uma nota.\n")
    n = int(input("Por favor, digite o número de notas a serem analisadas: "))

soma = 0

for i in range(1, n + 1):
    nota = float("-inf")
    while nota < 0:
        nota = float(input(f"Por favor, digite a nota {i}: "))
        if nota < 0:
            print("\n Uma nota não pode ser negativa. \n")
    soma += nota

media = soma / n

print(f"\nMédia aritmética das {n} notas: {media:.1f}")