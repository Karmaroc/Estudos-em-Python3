""" 
Peça ao usuário para digitar seu nome.
Peça ao usuário para digitar sua idade.

- Se o nome e a idade forem digitados, Exiba:

Seu nome é.
Seu nome invertido é.
Seu nome contém (ou não) espaços.
Seu nome tem {n} letras.
A primeira letra do seu nome é.
A última letra do seu nome é.

- Se nada for digitado em nome ou idade, Exiba:

"Desculpe, você deixou campos vazios."
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

if nome != '' and idade != '':
    print(10 * '-')
    print(f'Seu nome é: {nome}.')
    print(f'Seu nome invertido é: {nome[::-1]}.')
    print(f'Seu nome contém (ou não) espaços: {" " in nome}.')
    print(f'Seu nome tem {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}.')
    print(f'A última letra do seu nome é {nome[-1]}.')

else:
    if nome == '' and idade != '':
        print(10 * '-')
        print(f'Desculpe, mas você não digitou seu nome!') 
    elif nome != '' and idade == '':
        print(10 * '-')
        print(f'Desculpe, mas você não digitou a idade!') 
    else:
        print(10 * '-')
        print(f'Você deixou campos em aberto.')
        