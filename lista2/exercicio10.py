print("Exercício 10: Matutino, Vespertino ou Noturno?\n")

print("M - Matutino ; V - Vespertino ; N - Noturno")
turno = str(input("Digite a letra correspondente ao seu turno: ")).upper()

if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")