print("Exercício 14: Cálculo de uma multa por pesca em excesso")

peso_de_peixes = float(input("Digite o peso que João pescou ao todo: "))
excesso = 0
if peso_de_peixes > 50:
    excesso = peso_de_peixes - 50

multa = excesso * 4.00

print(f"Valor da multa que João deve pagar: {multa}")