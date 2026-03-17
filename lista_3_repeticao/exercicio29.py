print("Exercício 29: Loja do Sr. Manoel Joaquim\n")

itens = int(input("Digite o número de itens que o cliente levou, entre 1 e 50: "))
while itens <= 0 or itens > 50:
    print("\nO cliente deve levar pelo menos um item e no máximo cinquenta itens.\n")
    itens = int(input("Digite o número de itens que o cliente levou: "))

tabela = []
preco = 1.99

for i in range(1 , itens + 1):
    tabela.append(preco)
    preco += 1.99

print("\nLojas Quase Dois - Tabela de preços")
i = 1
for item in tabela:
    print(f"{i} - R$ {item:.2f}")
    i += 1