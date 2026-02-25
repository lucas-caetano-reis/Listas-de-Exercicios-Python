import math

print("Exercício 16: Calculadora do preço de um compra de tintas")

tamanho = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
cobertura = tamanho / 3 # 1 litro de tinta para cada 3 metros quadrados
numero_latas = math.ceil(cobertura / 18) # Uma lata tem 18 litros de tinta
preco_total = numero_latas * 80.00

print(f"Tamanho da área a ser pintada: {tamanho} metros quadrados")
print(f"Cobertura da parede: {cobertura} litros")
print(f"Número de latas necessárias: {numero_latas} latas")
print(f"Preço total: R$ {preco_total}")