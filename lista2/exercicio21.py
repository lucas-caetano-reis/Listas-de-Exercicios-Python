print("Exercício 21: Caixa Eletrônico")

saque = int(input("Por favor, insira o valor de saque entre 10 e 600 reais: "))
while saque < 10 and saque > 600:
    saque = int(input("Por favor, insira o valor de saque entre 10 e 600 reais: "))

notas100 = saque // 100
notas50 = (saque - notas100*100) // 50
notas10 = (saque - notas100*100 - notas50*50) // 10
notas5 = (saque - notas100*100 - notas50*50 - notas10*10) // 5
notas1 = (saque - notas100*100 - notas50*50 - notas10*10 - notas5*5)

print(f"Notas de 100 reais: {notas100}; notas de 50 reais: {notas50}; notas de 10 reais: {notas10}; notas de 5 reais: {notas5}; notas de 1 real: {notas1}")