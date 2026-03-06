print("Exercício 5: Aprovado ou reprovado?")

nota1 = float(input("Digite a nota parcial 1 do aluno: "))
while nota1 < 0 or nota1 > 10:
    nota1 = float(input("Digite a nota parcial 1 do aluno: "))

nota2 = float(input("Digite a nota parcial 2 do aluno: "))
while nota2 < 0 or nota2 > 10:
    nota2 = float(input("Digite a nota parcial 1 do aluno: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com distinção")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado")