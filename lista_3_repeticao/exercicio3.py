print("Exercício 3: Informações Pessoais\n")

nome = str(input("Por favor, insira um nome com no mínimo 4 caracteres: "))
while len(nome) < 4:
    print("Nome curto demais.\n")
    nome = str(input("Por favor, insira um nome com no mínimo 4 caracteres: "))

idade = int(input("\nPor favor, insira uma idade entre 0 e 150 anos: "))
while idade < 0 or idade > 150:
    print("Idade inválida.\n")
    idade = int(input("Por favor, insira uma idade entre 0 e 150 anos: "))

salario = float(input("\nPor favor, insira um salário maior que R$ 0.00: "))
while salario <= 0:
    print("Salário inválido.\n")
    salario = float(input("Por favor, insira um salário maior que R$ 0.00: "))

estado_civil = str(input("\nPor favor, insira seu estado civil - 's' para solteiro, 'c' para casado, 'v' para viúvo e 'd' para divorciado: ")).lower()
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    print("Estado inválido.\n")
    estado_civil = str(input("Por favor, insira seu estado civil - 's' para solteiro, 'c' para casado, 'v' para viúvo e 'd' para divorciado: ")).lower()

print("\nDados do usuário:")
print(f"Nome: {nome};")
print(f"Idade: {idade};")
print(f"Salário: {salario:.2f};")
print(f"Estado civil: {estado_civil}.")