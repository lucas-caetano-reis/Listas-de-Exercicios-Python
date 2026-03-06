import sys

print("Exercício 18: Verificador de datas dd/mm/aaaa")

dd = int(input("Insira o dia do mês: "))

if dd <= 0 or dd > 31:
    print("Dia inválido. Por favor, reinicie o programa.")
    sys.exit()

mm = int(input("Insira o mês do ano: "))

if mm <= 0 or mm > 12:
    print("Mês inválido. Por favor, reinicie o programa.")
    sys.exit()

aaaa = int(input("Insira o ano: "))

if aaaa <= 0:
    print("Ano inválido. Por favor, reinicie o programa.")
    sys.exit()

if mm == 2 or mm == 4 or mm == 6 or mm == 9 or mm == 11:
    if dd == 31:
        print("Data inválida. Fevereiro, abril, junho, setembro e novembro não possuem 31 dias.")
        sys.exit()

if mm == 2:
    if dd == 30:
        print("Data inválida. Fevereiro não possui 30 dias.")
        sys.exit()

if (aaaa % 4 != 0) or ((aaaa % 100 == 0) and (aaaa % 400 != 0)):
    if dd == 29:
        print("Data inválida. Fevereiro possui 29 dias apenas em anos bissextos.")
        sys.exit()

print(f"Data: {dd}/{mm}/{aaaa}")