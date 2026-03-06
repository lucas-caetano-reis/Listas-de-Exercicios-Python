print("Exercício 11: Reajuste de salário")

salario = float(input("Digite o seu salário: "))

reajuste = 0

if salario <= 280:
    reajuste = 0.20
elif salario > 280.00 and salario < 700.00:
    reajuste = 0.15
elif salario >= 700.00 and salario < 1500:
    reajuste = 0.10
else:
    reajuste = 0.05

aumento = salario * reajuste
salario_reajustado = salario + aumento

print(f"Salário antes do reajuste: {salario}")
print(f"Percentual do reajuste: {reajuste}")
print(f"Aumento: {aumento}")
print(f"Salário após o reajuste: {salario_reajustado}")