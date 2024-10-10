#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

import math

comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

area_paredes = 2 * (comprimento + largura) * altura  # Área total das 4 paredes
caixas_azulejos = math.ceil(area_paredes / 1.5)  # Quantidade de caixas de azulejos necessárias

print(f"\nÁrea total das paredes: {area_paredes:.2f} m²")
print(f"Quantidade de caixas de azulejos necessárias: {caixas_azulejos}")