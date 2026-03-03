print("Exercício 20: Média de três notas parciais")

nota1 = float(input("Por favor, insira a nota parcial 1 do aluno: "))
while nota1 < 0 or nota1 > 10:
    float(input("Por favor, insira a nota parcial 1 do aluno: "))

nota2 = float(input("Por favor, insira a nota parcial 2 do aluno: "))
while nota2 < 0 or nota2 > 10:
    float(input("Por favor, insira a nota parcial 2 do aluno: "))

nota3 = float(input("Por favor, insira a nota parcial 3 do aluno: "))
while nota3 < 0 or nota3 > 10:
    float(input("Por favor, insira a nota parcial 3 do aluno: "))

media = (nota1 + nota2 + nota3) / 3

print(f"Média do aluno: {media:.1f}")

if media == 10:
    print("Aprovado com distinção.")
elif media >= 7 and media < 10:
    print("Aprovado.")
else:
    print("Reprovado.")