tenho_sede = False

if tenho_sede:
    print("Beber agua")
    
print("Vida que segue")

esta_frio = False

if esta_frio:
    print("Vestir um casaco")
else:
    print("Vestir camiseta")
    
    
tenho_fome = False

if tenho_sede or tenho_fome:
    print("Vou na cozinha")
else:
    print("Ficar vendo netflix")
    

if tenho_sede and tenho_fome:
    print("Fazer sanduiche e coca")
else:
    print("não tenho fome ou não tenho sede")
  
    
if tenho_sede and tenho_fome:
    print("Fazer sanduiche e coca")
elif tenho_sede and not(tenho_fome):
    print ("tamar uma coquinha")
else:
    print("ficar vendo netflix")
    

num1 = 8
num2 = 5

if num1 == num2:
    print('num1 é igual a num2')
elif num1 > num2:
    print("num1 maior que num2")
elif num1 < num2:
    print("numero1 menor que numero2")
    
"""
Operadores Lógicos:

or, and, not

Operadores de comparação:

==, !=, >, <, >=, <= 
"""