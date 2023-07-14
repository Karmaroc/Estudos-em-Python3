""" 
Constantes 
"""
velocidade = int(input("Qual a velocidade do carro: "))
local_carro = int(input("Qual local o carro está: "))

RADAR = 60 #Velocidade máxima do radar
LOCAL = 100 #Local onde o radar está
RANGE = 1 #Distância do radar

range_99 = local_carro >= (LOCAL - RANGE)
range_101 = local_carro <= (LOCAL + RANGE)

if velocidade > RADAR:
    print('Velocidade do carro passou do RADAR.')
else:
    print('O carro não passou da velocidade do RADAR.')
    

if range_99 and range_101:
    print('Carro multado no RADAR.')
else:
    print('Carro não foi multado no RADAR.')