print("Exercício 11: Operações com números inteiros e reais")

numero_inteiro1 = int(input("Digite um número inteiro: "))
numero_inteiro2 = int(input("Digite um segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))

resposta1 = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
resposta2 = (3 * numero_inteiro1) + numero_real
resposta3 = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo: {resposta1}")
print(f"A soma do triplo do primeiro com o terceiro: {resposta2}")
print(f"O terceiro elevado ao cubo: {resposta3}")