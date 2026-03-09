print("Exercício 16: Série de Fibonacci até 500\n")

fibonacci = [1,1]
i = 1
termo = 0

while termo <= 500:
    termo = fibonacci[i - 1] + fibonacci[i]
    fibonacci.append(termo)
    i += 1

print(fibonacci)