print("\nExercício 38: Reajuste Salarial.\n")

ANO_DE_ENTRADA = int(1995)
ANO_ATUAL = int(2026)

while True:
    salario = float(input(f"Digite o valor do salário do funcionário no ano de {ANO_DE_ENTRADA}: "))
    
    reajuste = 0.015

    for i in range(ANO_DE_ENTRADA + 1, ANO_ATUAL + 1):
        salario *= (1 + reajuste)
        reajuste *= 2

    print(f"\nSalário atual em {ANO_ATUAL}: R$ {salario:.2f}\n")

    continuar = input("Deseja calcular novamente? (s/n): ").lower()
    if continuar != 's':
        break