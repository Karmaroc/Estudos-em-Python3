""" 
Flag - Marcar um local

is e is not 
id = Identidade
"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

condicao = True
passou = None

if condicao: 
    passou = True
    print("Go!")
else:
    print("Dont Go!")
    
print(passou, passou is None)

if passou is not None:
    print('Passou!')
else:
    print('Não passou!')