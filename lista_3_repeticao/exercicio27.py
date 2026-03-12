print("\nExercício 27: Número Médio de Alunos por Turma:\n")

turmas = int(input("Digite o número de turmas: "))
while turmas <= 0:
    print("\nDeve haver pelo menos uma turma\n.")
    turmas = int(input("Digite o número de turmas: "))
    
soma = 0

for i in range(1, turmas + 1):
    alunos = float("inf")
    while alunos > 40:
        alunos = int(input(f"Digite o número de alunos da turma {i}: "))
        if alunos > 40:
            print("\nAs turmas não podem ter mais que 40 alunos.\n")
    soma += alunos

media = int(soma / turmas)

print(f"\nMédia de alunos por turma: {media}.")