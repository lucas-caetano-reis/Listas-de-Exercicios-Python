print("Exercício 10: Intervalo Entre Dois Números")

numero1 = int(input("Por favor, insira um número inteiro qualquer: "))
numero2 = int(input("Por favor, insira um número inteiro que seja maior que número 1: "))
while numero1 >= numero2:
    numero2 = int(input("Por favor, insira um número inteiro que seja maior que número 1: "))

intervalo = []
for numero in range(numero1 + 1 , numero2):
    intervalo.append(numero)

print(f"\nNúmeros dentro do intervalo compreendido por {numero1} e {numero2}: {intervalo}")