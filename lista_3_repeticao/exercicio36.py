print("\nExercício 36: Tabuada de um Número Qualquer.\n")

numero = int(input("Montar a tabuada de: "))

comeco = int(input("Começar por: "))
if numero == 0:
    while comeco == 0:
        print("\nPor favor, digite um valor inicial diferente de 0.\n")
        comeco = int(input("Começar por: "))

termino = int(input("Terminar por: "))
while termino <= comeco:
    print("\nO valor final deve ser maior que o valor inicial.\n")
    termino = int(input("Terminar por: "))

print(f"\nVou montar a tabuada de {numero} começando em {comeco} e terminando em {termino}:")

for i in range (comeco, termino + 1):
    print(f"{numero} X {i} = {numero * i}")