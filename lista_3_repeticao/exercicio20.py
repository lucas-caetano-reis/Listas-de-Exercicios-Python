print("Exercício 20: Fatorial 2.0")

continuar = 1

while continuar == 1:
    inteiro = int(input("\nPor favor, insira um número inteiro positivo e menor que 16: "))
    while inteiro <= 0 or inteiro >= 16:
        inteiro = int(input("Por favor, insira um número inteiro positivo e menor que 16: "))
    
    fatorial = inteiro

    for i in range(inteiro - 1, 0, -1):
        fatorial *= i

    print(f"Fatorial de {inteiro}: {fatorial}")
    continuar = int(input("\nPor favor, digite 1 para continuar ou digite 0 para encerrar o programar: "))
    while continuar != 1 and continuar != 0:
        print("Valor inválido.\n")
        continuar = int(input("Por favor, digite 1 para continuar ou digite 0 para encerrar o programar: "))

    if continuar == 0:
        print("\nEncerrando o programa.")