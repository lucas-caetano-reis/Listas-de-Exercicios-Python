print("Exercício 24: Multioperações")

numero1 = float(input("Por favor, insira um número qualquer: "))
numero2 = float(input("Por favor, insira um número qualquer: "))

operacao = str(input("Por favor, escolha um tipo de operação: soma, subtração, multiplicação, divisão ou exponenciação: "))

if operacao == "soma":
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")
elif operacao == "subtração":
    resultado = numero1 - numero2
    print(f"Resultado: {resultado}")
elif operacao == "multiplicação":
    resultado = numero1 * numero2
    print(f"Resultado: {resultado}")
elif operacao == "divisão":
    resultado = numero1 / numero2
    print(f"Resultado: {resultado}")
elif operacao == "exponenciação":
    resultado = numero1 ** numero2
    print(f"Resultado: {resultado}")
else:
    print("Opção inválida. Por favor, rode o código novamente.\n")

if resultado % 2 == 0:
    print("Este número é par.\n")

else:
    print("Este número é ímpar.\n")

if resultado >= 0:
    print("Este número é positivo.\n")

else:
    print("Este número é negativo.\n")

resultado_arredondado = round(resultado)

if resultado == resultado_arredondado:
    print("Este número é inteiro.\n")

else:
    print("Este número é decimal.\n")