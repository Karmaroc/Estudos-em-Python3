""" 
Operadores in e not in

"""

nome = 'Otávio'

print(nome[2])
print(nome[-4])
print('O' in nome)
print('t' not in nome) # False

name = input("Digite uma palavra: ")
encontrar = input('Digite algo para encontrar: ')

if encontrar in name: 
    print("Encontrou", encontrar, name)
else:
    print("Não encontrou", encontrar, name)