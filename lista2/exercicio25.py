print("Exercício 25: 5 Perguntas para um Crime\n")

print("Responda sim ou não para as seguintes perguntas:\n")

resposta1 = str(input("Telefonou para a vítima? "))
resposta2 = str(input("Esteve no local do crime? "))
resposta3 = str(input("Mora perto da vítima? "))
resposta4 = str(input("Devia para a vítima? "))
resposta5 = str(input("Já trabalhou com a vítima? "))

respostas_suspeitas = 0

if resposta1 == "sim":
    respostas_suspeitas += 1

if resposta2 == "sim":
    respostas_suspeitas += 1

if resposta3 == "sim":
    respostas_suspeitas += 1

if resposta4 == "sim":
    respostas_suspeitas += 1

if resposta5 == "sim":
    respostas_suspeitas += 1

if respostas_suspeitas == 2:
    print("Esta pessoa parece suspeita.")
elif respostas_suspeitas == 3 or respostas_suspeitas == 4:
    print("Esta pessoa é provavelmente uma cúmplice.")
elif respostas_suspeitas == 5:
    print("Esta é provavelmente a assassina.")
else:
    print("Esta pessoa é inocente.")