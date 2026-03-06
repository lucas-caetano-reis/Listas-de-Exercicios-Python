print("Exercicio 15: Triângulos")

lado1 = float(input("Digite o valor do lado 1: "))
while lado1 <= 0:
    lado1 = float(input("Digite o valor do lado 1: "))

lado2 = float(input("Digite o valor do lado 2: "))
while lado2 <= 0:
    lado2 = float(input("Digite o valor do lado 2: "))

lado3 = float(input("Digite o valor do lado 3: "))
while lado3 <= 0:
    lado3 = float(input("Digite o valor do lado 3: "))

if ((lado1 + lado2) > lado3) or ((lado1 + lado3) > lado2) or ((lado3 + lado2) > lado1):
    triangulo = True
    print("\nO objeto é um triângulo\n")
else:
    print("Este objeto não é um triângulo")

if lado1 == lado2 and lado2 == lado3:
    print("Três lados iguais - Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Dois lados iguais - Triângulo Isósceles")
else:
    print("Três lados diferentes - Triângulo Escaleno")