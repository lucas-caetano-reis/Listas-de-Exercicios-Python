print("Exercício 4: Crescimento de Populações\n")

populacao_A = 80000
populacao_B = 200000

TAXA_CRESCIMENTO_A = 1.03
TAXA_CRESCIMENTO_B = 1.015

anos = 0

while populacao_A < populacao_B:
    anos += 1
    populacao_A *= TAXA_CRESCIMENTO_A
    populacao_B *= TAXA_CRESCIMENTO_B

    print(f"Ano: {anos}")
    print(f"Tamanho da população A: {populacao_A:.5f}")
    print(f"Tamanho da população B: {populacao_B:.5f}\n")