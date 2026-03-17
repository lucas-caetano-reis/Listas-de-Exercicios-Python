print("Exercício 31: Loja de Conveniências do Sr. Manoel Joaquim\n")

while True:
    preco = float('inf')
    precos = []
    total = 0

    i = 0

    while preco > 0:
        i += 1

        preco = float(input(f"Digite o preço do produto {i}: "))
        while preco < 0:
            print(f"\nO preço do produto {i} não pode ser negativo!\n")
            preco = float(input(f"Digite o preço do produto {i}: "))

        total += preco
        precos.append(preco)

    pagamento = float(input("Digite o valor em dinheiro fornecido pelo cliente: "))
    while pagamento < total:
        print(f"\nO valor em dinheiro não pode ser menor que o total de {total:.2f}!\n")
        pagamento = float(input("Digite o valor em dinheiro fornecido pelo cliente: "))

    troco = pagamento - total

    i = 0

    print(f"\nLojas Tabajara")
    for produto in precos:
        i += 1
        print(f"Produto {i}: R$ {produto:.2f}")
    print(f"Total: R$ {total:.2f}")
    print(f"Dinheiro: R$ {pagamento:.2f}")
    print(f"Troco: R$ {troco:.2f}")
    print(f"...\n")