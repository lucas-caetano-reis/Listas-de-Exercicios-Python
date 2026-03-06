import math

print("Exercício 17: Calculadora do preço de um compra de tintas")

tamanho = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
cobertura = tamanho / 6 # 1 litro de tinta para cada 6 metros quadrados

numero_latas = math.ceil(cobertura / 18) # Uma lata tem 18 litros de tinta
preco_latas = numero_latas * 80.00

numero_galoes = math.ceil(cobertura / 3.6)
preco_galoes = numero_galoes * 25.00

print("Caso 1: Apenas latas de 18 litros\n")

print(f"Tamanho da área a ser pintada: {tamanho} metros quadrados")
print(f"Cobertura da parede: {cobertura} litros")
print(f"Número de latas necessárias: {numero_latas} latas")
print(f"Preço total: R$ {preco_latas}\n")

print("Caso 2: Apenas galões de 3,6 litros\n")

print(f"Tamanho da área a ser pintada: {tamanho} metros quadrados")
print(f"Cobertura da parede: {cobertura} litros")
print(f"Número de galões necessários: {numero_galoes} galões")
print(f"Preço total: R$ {preco_galoes}\n")

print("Caso 3: Latas e galões, com desperdício mínimo de tinta")

cobertura_com_folga = cobertura * 1.1

numero_latas = int(cobertura_com_folga // 18)
resto = cobertura_com_folga - (numero_latas * 18)

if resto > 0:
    galoes = math.ceil(resto / 3.6)
else:
    galoes = 0

preco_latas = numero_latas * 80.00
preco_galoes = numero_galoes * 25.00
preco_total = preco_latas + preco_galoes

print(f"Tamanho da área a ser pintada: {tamanho} metros quadrados")
print(f"Cobertura da parede com folga de 10%: {cobertura_com_folga} litros")
print(f"Número de latas cheias: {numero_latas} latas")
print(f"Número de galões necessários: {numero_galoes} galões")
print(f"Preço total: R$ {preco_total}\n")