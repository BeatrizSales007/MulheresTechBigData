# 3) Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) 
# e que permitam realizar pedidos e fechar a conta.

def mostrar_cardapio():
    print("=== Cardápio ===")
    print("1. Hambúrguer - R$ 20.00")
    print("2. Pizza - R$ 30.00")
    print("3. Salada - R$ 15.00")
    print("4. Refrigerante - R$ 5.00")
    print("=================")

def realizar_pedido():
    total = 0
    while True:
        mostrar_cardapio()
        try:
            escolha = int(input("Escolha um item do cardápio (1-4) ou 0 para fechar a conta: "))
            if escolha == 0:
                break
            elif escolha == 1:
                total += 20.00
                print("Você pediu um Hambúrguer.")
            elif escolha == 2:
                total += 30.00
                print("Você pediu uma Pizza.")
            elif escolha == 3:
                total += 15.00
                print("Você pediu uma Salada.")
            elif escolha == 4:
                total += 5.00
                print("Você pediu um Refrigerante.")
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    
    return total

def fechar_conta(total):
    print(f"\nTotal da conta: R$ {total:.2f}")
    print("Obrigado e volte sempre!")

def main():
    total = realizar_pedido()
    fechar_conta(total)

if __name__ == "__main__":
    main()