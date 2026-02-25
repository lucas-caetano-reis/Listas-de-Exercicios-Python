print("Exercício 3: Masculino ou Feminino?")

letra = str(input("Digite uma letra qualquer do alfabeto: ")).upper()
if letra == "M":
    print(f"{letra} - Masculino")
elif letra == "F":
    print(f"{letra} - Feminino")
else:
    print(f"{letra} - Sexo inválido")