print("\nExercício 40: Estatísticas de Acidentes de Trânsito.\n")

mais_acidentes = float('-inf')
menos_acidentes = float('inf')

codigo_mais_acidentes = 0
codigo_menos_acidentes = 0

soma_veiculos = 0
soma_acidentes = 0
contador = 0

for i in range(1, 6):
    codigo = int(input(f"Digite o código da {i}° cidade: "))
    while codigo <= 0:
        print("\nO código da cidade deve ser superior a 0.\n")
        codigo = int(input(f"Digite o código da {i}° cidade: "))

    numero_veiculos = int(input(f"Digite o número de veículos de passeio (em 1999) na {i}° cidade: "))
    while numero_veiculos <= 0:
        print("\nO número de veículos de passeio da cidade deve ser superior a 0.\n")
        numero_veiculos = int(input(f"Digite o número de veículos de passeio (em 1999) na {i}° cidade: "))

    numero_acidentes = int(input(f"Digite o número de acidentes de trânsito com vítimas (em 1999) na {i}° cidade: "))
    while numero_acidentes <= 0:
        print("\nO número deve ser igual ou maior a 0.\n")
        numero_acidentes = int(input(f"Digite o número de acidentes de trânsito com vítimas (em 1999) na {i}° cidade: "))

    if numero_acidentes > mais_acidentes:
        mais_acidentes = numero_acidentes
        codigo_mais_acidentes = codigo

    if numero_acidentes < menos_acidentes:
        menos_acidentes = numero_acidentes
        codigo_menos_acidentes = codigo

    soma_veiculos += numero_veiculos

    if numero_veiculos < 2000:
        contador += 1
        soma_acidentes += numero_acidentes

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes / contador

print("\nEstatísticas de Trânsito em 5 Cidades:\n")
print(f"Maior índice de acidentes: {mais_acidentes}; Código da cidade: {codigo_mais_acidentes}")
print(f"Menor índice de acidentes: {menos_acidentes}; Código da cidade: {codigo_menos_acidentes}")
print(f"Média de veículos nas 5 cidades juntas: {media_veiculos}")
print(f"Média de acidentes de trânsito nas cidades com menos de 2000 veículos de passeio: {media_acidentes}")