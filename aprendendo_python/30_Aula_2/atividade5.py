""" 
Iterando strings com while
"""
nome = 'Vitor Manoel'

contador = 0
nova_string = ''

while contador < (len(nome)):
    letra = nome[contador]
    nova_string += f'*{letra}'
    contador += 1

nova_string += '*'
print(nova_string)