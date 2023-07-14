"""
Operadores de atribuição:
=, +=, -=, *=, /=, //=, **=, %=
"""
# Múltiplos de 2 até 1000.
"""
contador = 1

while contador <= 1024:
    print(contador)
    contador *= 2
    
print('Acabou!')
"""

contador1 = 0

while contador1 <= 150:
    contador1 += 1
    
    if contador1 == 8:
        print("Não vou mostrar o 8")
        continue
    
    if contador1 >= 50 and contador1 <= 99:
        print('Não vou mostrar o', contador1)
        continue

    print(contador1)
    
    if contador1 == 100:
        break