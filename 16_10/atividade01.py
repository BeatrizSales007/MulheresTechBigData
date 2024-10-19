# 1) Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. Crie uma função para calcular a multa, se aplicável.


def calcular_multa():
    peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
    peso_maximo = 100  
    valor_multa_por_quilo = 10  
    
    if peso_peixes > peso_maximo:
        excesso = peso_peixes - peso_maximo
        multa = excesso * valor_multa_por_quilo
        print(f"O pescador deve pagar uma multa de R$ {multa:.2f}.")
    else:
        print("O pescador não precisa pagar multa.")

calcular_multa()