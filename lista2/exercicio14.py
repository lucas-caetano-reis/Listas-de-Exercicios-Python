print("Exercicio 14: Medias das notas parciais")

np1 = float(input("Digita a nota parcial 1 do aluno: "))
while np1 < 0 or np1 > 10:
    np1 = float(input("Digita a nota parcial 1 do aluno: "))

np2 = float(input("Digita a nota parcial 2 do aluno: "))
while np2 < 0 or np2 > 10:
    np2 = float(input("Digita a nota parcial 2 do aluno: "))

media = (np1 + np2) / 2

if media >= 0 and media < 4.0:
    conceito = "E"
    print("Média de Aproveitamento entre 0 e 4.0 - Conceito: E")
elif media >= 4.0 and media < 6.0:
    conceito = "D"
    print("Média de Aproveitamento entre 4.0 e 6.0 - Conceito: D")
elif media >= 6.0 and media < 7.5:
    conceito = "C"
    print("Média de Aproveitamento entre 6.0 e 7.5 - Conceito: C")
elif media >= 7.5 and media < 9.0:
    conceito = "B"
    print("Média de Aproveitamento entre 7.5 e 9.0 - Conceito: B")
elif media >= 9.0 and media <= 10:
    conceito = "A"
    print("Média de Aproveitamento entre 9.0 e 10.0 - Conceito: A")

if conceito == "A" or conceito == "B" or conceito == "C":
    print("Aprovado")
else:
    print("Reprovado")