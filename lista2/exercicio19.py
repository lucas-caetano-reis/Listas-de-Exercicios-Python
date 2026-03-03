print("Exercício 19: Centenas, dezenas e unidades")

numero = int(input("Por favor, insira um número inteiro menor que 1000: "))
while numero >= 1000:
    numero = int(input("Por favor, insira um número inteiro menor que 1000: "))

centenas = numero // 100
dezenas = (numero - (centenas*100)) // 10
unidades = (numero - (centenas*100) - (dezenas*10))

if centenas > 1 and dezenas > 1 and unidades > 1:
    print(f"{centenas} centenas, {dezenas} dezenas e {unidades} unidades")

elif centenas > 1 and dezenas > 1 and unidades == 1:
    print(f"{centenas} centenas, {dezenas} dezenas e {unidades} unidade")

elif centenas > 1 and dezenas > 1 and unidades == 0:
    print(f"{centenas} centenas e {dezenas} dezenas")

elif centenas > 1 and dezenas == 1 and unidades > 1:
    print(f"{centenas} centenas, {dezenas} dezena e {unidades} unidades")

elif centenas > 1 and dezenas == 1 and unidades == 1:
    print(f"{centenas} centenas, {dezenas} dezena e {unidades} unidade")

elif centenas > 1 and dezenas == 1 and unidades == 0:
    print(f"{centenas} centenas e {dezenas} dezena")

elif centenas > 1 and dezenas == 0 and unidades > 1:
    print(f"{centenas} centenas e {unidades} unidades")

elif centenas > 1 and dezenas == 0 and unidades == 1:
    print(f"{centenas} centenas e {unidades} unidade")

elif centenas > 1 and dezenas == 0 and unidades == 0:
    print(f"{centenas} centenas")

elif centenas == 1 and dezenas > 1 and unidades > 1:
    print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidades")

elif centenas == 1 and dezenas > 1 and unidades == 1:
    print(f"{centenas} centena, {dezenas} dezenas e {unidades} unidade")

elif centenas == 1 and dezenas > 1 and unidades == 0:
    print(f"{centenas} centena e {dezenas} dezenas")

elif centenas == 1 and dezenas == 1 and unidades > 1:
    print(f"{centenas} centena, {dezenas} dezena e {unidades} unidades")

elif centenas == 1 and dezenas == 1 and unidades == 1:
    print(f"{centenas} centena, {dezenas} dezena e {unidades} unidade")

elif centenas == 1 and dezenas == 1 and unidades == 0:
    print(f"{centenas} centena e {dezenas} dezena")

elif centenas == 1 and dezenas == 0 and unidades > 1:
    print(f"{centenas} centena e {unidades} unidades")

elif centenas == 1 and dezenas == 0 and unidades == 1:
    print(f"{centenas} centena e {unidades} unidade")

elif centenas == 1 and dezenas == 0 and unidades == 0:
    print(f"{centenas} centena")

elif centenas == 0 and dezenas > 1 and unidades > 1:
    print(f"{dezenas} dezenas e {unidades} unidades")

elif centenas == 0 and dezenas > 1 and unidades == 1:
    print(f"{dezenas} dezenas e {unidades} unidade")

elif centenas == 0 and dezenas > 1 and unidades == 0:
    print(f"{dezenas} dezenas")

elif centenas == 0 and dezenas == 1 and unidades > 1:
    print(f"{dezenas} dezena e {unidades} unidades")

elif centenas == 0 and dezenas == 1 and unidades == 1:
    print(f"{dezenas} dezena e {unidades} unidade")

elif centenas == 0 and dezenas == 1 and unidades == 0:
    print(f"{dezenas} dezena")

elif centenas == 0 and dezenas == 0 and unidades > 1:
    print(f"{unidades} unidades")

elif centenas == 0 and dezenas == 0 and unidades == 1:
    print(f"{unidades} unidade")

elif centenas == 0 and dezenas == 0 and unidades == 0:
    print(f"0")