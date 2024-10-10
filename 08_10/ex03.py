# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

odometro_inicio = float(input("Marcação do odômetro no início do dia (km): "))
odometro_fim = float(input("Marcação do odômetro no final do dia (km): "))
litros_gastos = float(input("Número de litros de combustível gasto: "))
valor_total = float(input("Valor total (R$) recebido dos passageiros: "))

distancia_percorrida = odometro_fim - odometro_inicio
media_consumo = distancia_percorrida / litros_gastos
lucro = valor_total - (litros_gastos * 4.87)  # Custo do combustível

print(f"\nMédia de consumo: {media_consumo:.2f} km/L")
print(f"Lucro líquido do dia: R$ {lucro:.2f}")