###ATIVIDADE###
# Crie um código que seja capaz de ler e armazenar uma sequência de 20 números pares e 20 números ímpares.
# Obs: utilize estruturas de repetição para fechar esse conjunto de números.

numeros_pares = []
numeros_impares = []


while len(numeros_pares) < 20 or len(numeros_impares) < 20:
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        if len(numeros_pares) < 20:
            numeros_pares.append(numero)
            print("O número é par.")
        else:
            print("Já foram coletados 20 números pares. Digite um número ímpar.")
    else:
        if len(numeros_impares) < 20:
            numeros_impares.append(numero)
            print("O número é ímpar.")
        else:
            print("Já foram coletados 20 números ímpares. Digite um número par.")

def exibir_numeros():
    while True:
        escolha = input("Deseja ver os valores 'pares' ou 'ímpares'? ").strip().lower()
        
        if escolha == 'pares':
            print("Números pares:", numeros_pares)
        elif escolha == 'ímpares':
            print("Números ímpares:", numeros_impares)
        else:
            print("Opção inválida. Por favor, escolha 'pares' ou 'ímpares'.")
            continue
        
        retornar = input("Deseja retornar e ver os outros valores? (sim/não) ").strip().lower()
        if retornar == 'não':
            break


exibir_numeros()