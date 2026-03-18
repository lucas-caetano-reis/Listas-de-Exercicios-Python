print("\nExercício 39: Aluno Mais Baixo e Aluno Mais Alto Entre 10 Alunos.\n")

maior_altura = float('-inf')
menor_altura = float('inf')

numero_aluno_mais_alto = 0
numero_aluno_mais_baixo = 0

for i in range(1, 11):
    numero = int(input(f"Digite o número do {i}° aluno: "))
    while numero <= 0:
        print("\nO número do aluno deve ser maior do que 0.\n")
        numero = int(input(f"Digite o número do {i}° aluno: "))

    altura = int(input(f"Digite a altura do {i}° aluno em centímetros: "))
    while altura <= 0:
        print("\nA altura do aluno deve ser maior do que 0.\n")
        altura = int(input(f"Digite a altura do {i}° aluno em centímetros: "))

    if altura > maior_altura:
        maior_altura = altura
        numero_aluno_mais_alto = numero

    if altura < menor_altura:
        menor_altura = altura
        numero_aluno_mais_baixo = numero

print("\nCenso do Colégio:\n")
print(f"Número do aluno mais alto: {numero_aluno_mais_alto}; Altura: {maior_altura}")
print(f"Número do aluno mais baixo: {numero_aluno_mais_baixo}; Altura: {menor_altura}")