""" 
Operadores Lógicos

and (e) or (ou) not (não)

and - Todas as condições precisam ser verdadeiros.

"""

entrada = input("[E]ntrar [S]air: ")

senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Login feito com sucesso!')
else: 
    print('Sair')
    
print(True and True)
print(True and False)