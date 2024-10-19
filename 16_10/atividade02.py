# 2) Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do
# IMC, mostrando ao final a classificação de acordo com a tabela de IMC.

def calcular_imc():
    peso = float(input("Qual o peso da pessoa (em kg)? "))
    altura = float(input("Qual a altura da pessoa (em metros)? "))
    
    imc = peso / (altura ** 2)
    
    print(f"O IMC da pessoa é: {imc:.2f}")
    
    if imc < 18.5:
        classificacao = "Magreza"
    elif 18.5 <= imc < 24.9:
        classificacao = "Normal"
    elif 25 <= imc < 29.9:
        classificacao = "Sobrepeso"
    elif 30 <= imc < 39.9:
        classificacao = "Obesidade"
    else:
        classificacao = "Obesidade grave"
    
    print(f"Classificação: {classificacao}")

calcular_imc()