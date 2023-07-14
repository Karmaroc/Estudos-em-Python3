"""
Try/except
"""
print('Teste 1')
print('Teste 2')

numero = input('Digite um número: ')
print(type(numero))
# numero_float = float(numero)
print(f'O triplo de {numero} é {numero * 3}.')

try:
    x = int(numero)
    print('Número.', x)
    
except:
    print('Não pode converter str em int.')

