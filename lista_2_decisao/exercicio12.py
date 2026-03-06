print("Exercício 12: Cálculo da folha de pagamento")

horas = int(input("Digite o número de horas trabalhadas: "))
pagamento = float(input("Digite o pagamento dado por horas trabalhadas: "))

salario_bruto = horas * pagamento

if salario_bruto <= 900:
    ir = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir = 0.05
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir = 0.10
else:
    ir = 0.20

INSS = 0.10
FGTS = 0.11

desconto_ir = salario_bruto * ir
desconto_inss = salario_bruto * INSS
desconto_fgts = salario_bruto * FGTS

descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - descontos

print(f"Salário bruto: ({horas} * {pagamento}) : R$ {salario_bruto}")
print(f"(-) Imposto de renda ({ir * 100}%) : R$ {desconto_ir}")
print(f"(-) INSS ({INSS * 100}%) : R$ {desconto_inss}")
print(f"FGTS ({FGTS * 100}%) : R$ {desconto_fgts}")
print(f"Total de descontos : R$ {descontos}")
print(f"Salário líquido :  R$ {salario_liquido}")