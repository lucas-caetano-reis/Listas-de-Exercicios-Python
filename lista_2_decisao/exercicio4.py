print("Exercício 4: Vogal ou Consoante?")

letra = str(input("Digite uma letra qualquer do alfabeto: ")).upper()

if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")