print("Exercício 13: Conversor Gigabytes para Megabytes e Kilobytes")

Gigabytes = float(input("Digite o tamanho de um arquivo em gigabytes: "))
Megabytes = Gigabytes * 1024
Kilobytes = Megabytes * 1024

print(f"Tamanho do arquivo em megabytes: {Megabytes}")
print(f"Tamanho do arquivo em kilobytes: {Kilobytes}")