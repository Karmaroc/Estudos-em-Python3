""" 
Operador Lógico

or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.

"""

entrada = input('[E, e]ntrar ou [S, s]air: ')
senha_digitada = input('Senha: ')

senha = 'vitor'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha):
    print('Entrei.')
else:
    print('Saí.')
    
# Avaliação de curto circuito

print(True or False or 0)

senha1 = input('Outra senha: ') or 'Não tem senha'
print(senha1)