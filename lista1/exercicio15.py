print("Exercício 15: Calculadora do quanto o estado toma do seu salário")

pagamento = float(input("Por favor insira o valor que você ganha por hora trabalhada: "))
horas = float(input("Por favor insira o número de horas trabalhadas nesse mês: "))

salario_bruto = pagamento * horas

imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = imposto_de_renda + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f"+ Salário Bruto : R$ {salario_bruto}")
print(f"- Imposto de Renda (11%) : R$ {imposto_de_renda}")
print(f"- INSS (8%) : R$ {inss}")
print(f"- Sindicato ( 5%) : R$ {sindicato}")
print(f"= Salário Liquido : R$ {salario_liquido}")