# Desenvolva um programa que guarde os dados de 10 pessoas que estão se candidatando a uma vaga de emprego, sabendo que candidatos 
# menores de 18 anos não podem participar. Os dados coletados são: nome, data de nascimento, telefone, e-mail, formação acadêmica e a 
# experiência profissional.

while True:
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    
    if idade < 18:
        print("Menor de 18 anos não pode se candidatar.")
        
    else:
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        formacao = input("Formação Acadêmica: ")
        experiencia = input("Experiência Profissional: ")

        print(f"\nCandidato cadastrado: Nome: {nome}, Idade: {idade}, Telefone: {telefone}, E-mail: {email}, Formação: {formacao}, Experiência: {experiencia}")
        
        if input("\nDeseja cadastrar mais um candidato? (s/n): ").lower() != 's':
            break
