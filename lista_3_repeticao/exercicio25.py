print("Exercício 25: Média de Idade de N Pessoas\n")

n = int(input("Por favor, digite o número de pessoas da turma: "))
while n <= 0:
    print("\nDeve haver pelo menos uma pessoa na turma.\n")
    n = int(input("Por favor, digite o número de pessoas da turma: "))

soma = 0

for i in range(1 , n + 1):
    idade = float("-inf")
    while idade < 0:
        idade = int(input(f"Por favor, digite a idade da pessoa número {i}: "))
        if idade < 0:
            print("\nA idade não pode ser negativa.\n")
    soma += idade

media = int(soma / n)

print(f"\nMédia de idade da turma de {n} pessoas: {media}")

if media >= 0 and media <= 25:
    print("Esta turma é jovem.")
elif media > 25 and media <= 60:
    print("Esta turma é adulta.")

else:
    print("Esta turma é idosa.")