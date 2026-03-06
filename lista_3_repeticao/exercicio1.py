print("Exercício 1: Informe o valor válido\n")

valor = int(input("Por favor, insira um valor entre 0 e 10: "))
while valor < 0 or valor > 10:
    print("Valor inválido.\n")
    valor = int(input("Por favor, insira um valor entre 0 e 10: "))

print(f"Valor válido.")