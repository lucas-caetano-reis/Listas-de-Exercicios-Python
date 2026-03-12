print("Exercício 26: Eleições\n")

eleitores = int(input("Por favor, digite o número de eleitores: "))
while eleitores <= 0:
    print("Deve haver pelo menos um eleitor.")
    eleitores = int(input("Por favor, digite o número de eleitores: "))

votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0

print("\nExistem 3 candidatos nessas eleições e seus números são 1, 2 e 3.\n")

for i in range(1 , eleitores + 1):
    voto = ""
    while voto != "1" and voto != "2" and voto != "3":
        voto = str(input(f"Digite o número do candidato votado pelo eleitor número {i}: "))
        if voto == "1":
            votos_candidato_1 += 1
        elif voto == "2":
            votos_candidato_2 += 1
        elif voto == "3":
            votos_candidato_3 += 1
        else:
            print(f"\nVoto inválido. Os números dos candidatos são 1, 2 e 3.\n")

print(f"\nResultados das Eleições:")
print(f"O candidato 1 recebeu {votos_candidato_1}.")
print(f"O candidato 2 recebeu {votos_candidato_2}.")
print(f"O candidato 3 recebeu {votos_candidato_3}.")