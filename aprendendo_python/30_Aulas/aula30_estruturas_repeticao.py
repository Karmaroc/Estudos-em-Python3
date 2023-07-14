""" 
Repetições:

while(enquanto)

Executa uma ação enquanto uma condição for verdadeira
"""
tentativa_numeros = 0

while tentativa_numeros != 'sair':
    print(30 * '#')
    tentar = input('Digite "sair" para sair: ')
    tentativa_numeros = tentar
    
    if tentar.isdigit():
        print(f'As tentativas são {tentar}.')
    
    elif type(tentar) == type(""):
        print(f'Você digitou uma string {tentar}.')
    
    else:
        if tentar == 'sair':
            print(f'Você digitou "{tentativa_numeros}" e saiu.')
    
    