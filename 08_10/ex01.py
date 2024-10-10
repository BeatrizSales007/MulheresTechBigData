# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;



#variáveis simples - são as que calculam a entrada de dados
potencia_lampada = float(input("Digite a potência da lâmpada (em watts): ")) 
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))


# variáveis para o cálculo de área e de potência
area = largura * comprimento
potencia_necessaria = potencia_lampada * 3
numero_lampadas =int(potencia_necessaria / potencia_lampada)
bocais_disponiveis = area / 3

print(f"\nÁrea do cômodo: {area:.2f} m²")
print(f"Potência total necessária: {potencia_necessaria:.2f} watts")
print(f"Número de lâmpadas necessárias: {numero_lampadas}")
print(f"Bocais disponíveis: {bocais_disponiveis:.2f}")
print("É possível instalar todas as lâmpadas." if numero_lampadas <= bocais_disponiveis else "Não há bocais suficientes para todas as lâmpadas.")