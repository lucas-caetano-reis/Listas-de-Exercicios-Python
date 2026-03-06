import sys

print("Exercício 26: Posto de Gasolina")

litros = int(input("Por favor, insira o valor dos litros de combustível: "))
combustivel = str(input("Por favor, escolha o tipo de combustível - A para álcool e G para gasolina: ")).upper()

if combustivel == "A":
    if litros <= 20:
        preco = litros * 1.9 - 0.03 * litros
    else:
        preco = litros * 1.9 - 0.05 * litros

elif combustivel == "G":
    if litros <= 20:
        preco = litros * 2.5 - 0.04 * litros
    else:
        preco = litros * 2.5 - 0.06 * litros

else:
    print("Opção inválida. Por favor, rode o código novamente.")
    sys.exit()

print(f"Preço calculado: {preco}")