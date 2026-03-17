print("Exercício 30: Panificadora do Sr. Manoel Joaquim\n")

paes = int(input("Digite o número de pães que o cliente levou, entre 1 e 50: "))
while paes <= 0 or paes > 50:
    print("\nO cliente deve levar pelo menos um pão e no máximo cinquenta pães.\n")
    paes = int(input("Digite o número de pães que o cliente levou: "))

tabela = []
preco = 0.18

for i in range(1 , paes + 1):
    tabela.append(preco)
    preco += 0.18

print("\nPanificadora Pão de Ontem - Tabela de preços")
i = 1
for pao in tabela:
    print(f"{i} - R$ {pao:.2f}")
    i += 1