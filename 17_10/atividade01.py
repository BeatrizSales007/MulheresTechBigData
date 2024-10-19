#Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente. Utilize 
#tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR, ter uma exceção personalizada.

class NumeroImparError(Exception):
    pass

def ler_par_de_numeros():
    while True:
        try:
            num1 = int(input("Digite o primeiro número (inteiro): "))
            num2 = int(input("Digite o segundo número (inteiro): "))
            
            if num1 % 2 != 0 or num2 % 2 != 0:
                raise NumeroImparError("Um ou ambos os números são ímpares. Por favor, insira números pares.")
            
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, insira apenas números inteiros.")
        except NumeroImparError as e:
            print(e)

def calcular_somas():
    for i in range(3):
        print(f"\nPar {i + 1}:")
        num1, num2 = ler_par_de_numeros()
        soma = num1 + num2
        
        print(f"A soma de {num1} e {num2} é: {soma}")

calcular_somas()