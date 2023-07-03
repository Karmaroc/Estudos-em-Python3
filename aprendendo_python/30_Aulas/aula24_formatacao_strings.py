""" 
Formatação básica de strings

s - string
d - int
f - float
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:0>10}') # Preenchendo espaços
print(f'{1000.32234324:+.2f}') # Diminuindo casas decimais
print(f'O hexadecimal de 750 é {750:05X}')