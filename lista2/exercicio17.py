print("Exercício 17: Anos bissextos")

ano = int(input("Por favor, insira um ano para a análise: "))

if (ano % 4) == 0 and (ano % 100) != 0:
    print("O ano é bissexto.")
elif (ano % 400) == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")