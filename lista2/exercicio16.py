import sys, math

print("Exercício 16: Raízes de uma equação de segundo grau")
# Equação de segundo grau: ax2 + bx + c

a = int(input("Insira o valor da variável a: "))

if a == 0:
    print("Equação de primeiro grau. Por favor, reinicie o programa.")
    sys.exit()

b = int(input("Insira o valor da variável b: "))
c = int(input("Insira o valor da variável c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais. Por favor, reinicie o programa.")
    sys.exit()

elif delta == 0:
    raiz = ((-b) + math.sqrt(delta)) / (2*a)
    print(f"A equação possui apenas uma raíz real: {raiz:.2f}")

else:
    raiz1 = ((-b) + math.sqrt(delta)) / (2*a)
    raiz2 = ((-b) - math.sqrt(delta)) / (2*a)
    print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")