# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.


valor = float(input("Digite um valor: "))

if valor >= 0:
    resultado = "Positivo"
else:
    resultado = "Negativo"

print(f"O valor é: {resultado}")