print("Exercício 18: Programa que calcula o tempo de download de um arquivo")

tamanho_arquivo = float(input("Digite o tamanho do arquivo em megabytes:"))
velocidade = float(input("Digite da velocidade de download em megabytes por segundo: "))

tempo_de_download = (tamanho_arquivo / velocidade) / 60 # O tempo de download deve ser em minutos

print(f"O tempo de download do arquivo será de {tempo_de_download} minutos")