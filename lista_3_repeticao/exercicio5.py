print("Exercício 5: Crescimento de Populações 2")

continuar = 1

while continuar == 1:
    populacao_A = int(input("\nPor favor, insira um valor maior que 0 para a população A: "))
    while populacao_A <= 0:
        print("Valor inválido.\n")
        populacao_A = int(input("Por favor, insira um valor maior que 0 para a população A: "))

    populacao_B = int(input("Por favor, insira um valor maior que a população A para a população B: "))
    while populacao_A >= populacao_B:
        print("Valor inválido.\n")
        populacao_B = int(input("Por favor, insira um valor maior que a população A para a população B: "))

    taxa_crescimento_a = float(input("Por favor, insira um valor decimal maior que 0 para a taxa de crescimento da população A: "))
    while taxa_crescimento_a <= 0:
        print("Valor inválido.\n")
        taxa_crescimento_a = float(input("Por favor, insira um valor decimal maior que 0 para a taxa de crescimento da população A: "))

    taxa_crescimento_b = float(input("Por favor, insira um valor decimal menor que a taxa de crescimento da população A para a taxa de crescimento da população B: "))
    while taxa_crescimento_b >= taxa_crescimento_a:
        print("Valor inválido.\n")
        taxa_crescimento_b = float(input("Por favor, insira um valor decimal menor que a taxa de crescimento da população A para a taxa de crescimento da população B: "))

    anos = 0

    while populacao_A < populacao_B:
        anos += 1
        populacao_A *= taxa_crescimento_a
        populacao_B *= taxa_crescimento_b

    print(f"Ano: {anos}")
    print(f"Tamanho da população A: {populacao_A:.5f}")
    print(f"Tamanho da população B: {populacao_B:.5f}\n")

    continuar = int(input("Digite '1' para repetir a operação ou digite '0' para encerrar o script: "))
    while continuar != 1 and continuar != 0:
        print("Opção inválida.\n")
        continuar = int(input("Digite '1' para repetir a operação ou digite '0' para encerrar o script: "))

    if continuar == 0:
        print("Sistema encerrado.")