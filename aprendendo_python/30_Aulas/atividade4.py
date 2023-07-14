""" 
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")
 
if not numero.isdigit():
    print("Não é um número inteiro.")
    
elif int(numero) % 2 == 0:
    print(f"O número {numero} é Par!")
    
else:
    if int(numero) % 2 != 0:
        print(f"O número {numero} é Ímpar!")
        
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:

Bom dia 0-11, Boa Tarde 12-17 e Boa Noite 18-23.
"""
print(50 * "-")

horas = input("Quantas horas? Digite um número entre 0 e 23: ")

if not (horas.isdigit()) or int(horas) > 23:
    print("Não é uma hora.")
    
elif int(horas) >= 0 and int(horas) <= 11:
    print("Bom Dia 0-11.")

elif int(horas) <= 17:
    print("Boa Tarde 12-17.")

else:
    if int(horas) <= 23:
        print("Boa Noite 18-23.")
        
""" 
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande."
"""
print(50 * "-")

nome = input("Qual o seu primeiro nome: ")

if nome == '':
    print("Não é um nome, mas vázio.")
    
elif nome.isdigit():
    print("Não é um nome, mas um número.")
    
elif len(nome) > 0 and len(nome) <= 4:
    print("Seu nome é curto.")
    
elif len(nome) >= 5 and len(nome) <= 6:
    print("Seu nome é normal.")
    
else:
    if len(nome) > 6:
        print("Seu nome é muito grande.")

    