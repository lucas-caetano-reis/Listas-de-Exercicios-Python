print("\nExercício 37: Censo de uma Academia.\n")

maior_altura = float('-inf')
menor_altura = float('inf')
maior_peso = float('-inf')
menor_peso = float('inf')

codigo_mais_alto = 0
codigo_mais_baixo = 0
codigo_mais_gordo = 0
codigo_mais_magro = 0

soma_alturas = 0
soma_pesos = 0

i = 0

while True:
    i += 1
    codigo = int(input(f"Digite o código do cliente {i} (0 para sair): "))
    while codigo < 0:
        print("\nO código deve ser maior ou igual a 0.\n")
        codigo = int(input(f"Digite o código do cliente {i} (0 para sair): "))


    if codigo == 0:
        break

    altura = float(input(f"Digite a altura do cliente {i}: "))
    while altura <= 0:
        print("\nA altura deve ser superior a 0.\n")
        altura = float(input(f"Digite a altura do cliente {i}: "))

    if altura > maior_altura:
        maior_altura = altura
        codigo_mais_alto = codigo
    if altura < menor_altura:
        menor_altura = altura
        codigo_mais_baixo = codigo

    soma_alturas += altura

    peso = float(input(f"Digite o peso do cliente {i}: "))
    while peso <= 0:
        print("\nO peso deve ser superior a 0.\n")
        peso = float(input(f"Digite o peso do cliente {i}: "))

    if peso > maior_peso:
        maior_peso = peso
        codigo_mais_gordo = codigo
    if peso < menor_peso:
        menor_peso = peso
        codigo_mais_magro = codigo

    soma_pesos += peso

if i > 0:
    media_alturas = soma_alturas / i
    media_pesos = soma_pesos / i

    print("\nCenso da Academia:")
    print(f"Mais alto: {codigo_mais_alto}; Altura: {maior_altura:.2f}")
    print(f"Mais baixo: {codigo_mais_baixo}; Altura: {menor_altura:.2f}")
    print(f"Mais gordo: {codigo_mais_gordo}; Peso: {maior_peso:.2f}")
    print(f"Mais magro: {codigo_mais_magro}; Peso: {menor_peso:.2f}")
    print(f"Média das alturas: {media_alturas:.2f}")
    print(f"Média dos pesos: {media_pesos:.2f}")

else:
    print("Nenhum cliente cadastrado.")