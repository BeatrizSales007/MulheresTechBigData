# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, 
# deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a  nota mais baixa entre as duas primeiras avaliações.
# Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (ou -1 se não feita): "))

if nota_optativa == -1:
    media = (nota1 + nota2) / 2
else:
    menor_nota = min(nota1, nota2)
    media = (nota1 + nota2 + nota_optativa - menor_nota) / 2

if media >= 6.0:
    situacao = "Aprovado"
elif media < 3.0:
    situacao = "Reprovado"
else:
    situacao = "Em exame"

print(f"Média do semestre: {media:.2f}")
print(situacao)
