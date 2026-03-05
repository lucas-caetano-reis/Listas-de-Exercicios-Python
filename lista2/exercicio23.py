print("Exercício 23: Inteiro ou Decimal?")

numero = float(input("Por favor, insira um número qualquer: "))

numero_arredondado = round(numero)

print(f"Número antes do arredondamento: {numero}")
print(f"Número depois do arredondamento: {numero_arredondado}\n")

if numero == numero_arredondado:
    print("Este número é inteiro.")

else:
    print("Este número é decimal.")