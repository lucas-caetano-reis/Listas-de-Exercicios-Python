print("\nExercício 28: Gastos com uma Coleção de CDs\n")

cds = int(input("Digite o tamanho da coleção: "))
while cds <= 0:
    print("\nA coleção não pode estar vazia ou ter tamanho negativo.\n")
    cds = int(input("Digite o tamanho da coleção: "))

gasto_total = 0

for i in range(1, cds + 1):
    preco = 0
    while preco <= 0:
        preco = float(input(f"Digite o preço do {i}° CD: "))
        if preco <= 0:
            print("\nO preço de um CD deve ser maior do que 0.\n")
    gasto_total += preco

media = gasto_total / cds

print(f"\nValor médio gasto na compra de todos os CDs da coleção: R${media:.2f}")