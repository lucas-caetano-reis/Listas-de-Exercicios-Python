print("Exercício 2: Cadastro de Usuário\n")

nome = str(input("Por favor, insira um nome de usuário: "))
senha = str(input("Por favor, insira uma senha diferente de seu nome de usuário: "))

while senha == nome:
    print("Senha inválida.\n")

    nome = str(input("Por favor, insira um nome de usuário: "))
    senha = str(input("Por favor, insira uma senha diferente de seu nome de usuário: "))

print(f"\nNome de usuário: {nome}")
print(f"Senha do usuário: {senha}")