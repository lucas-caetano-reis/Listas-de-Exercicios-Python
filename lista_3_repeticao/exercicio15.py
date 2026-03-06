print("Exercício 15: Série de Fibonacci\n")

n = int(input("Por favor, insira um número inteiro qualquer para servir de n-ésimo termo: "))

fibonacci = [1,1]

for i in range(1, n + 1):
    termo = fibonacci[i] + fibonacci[i - 1]
    fibonacci.append(termo)

print(fibonacci)