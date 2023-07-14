string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]
    print(letra)
    
    i = i + 1
    break

else:
    print('O else foi executado.')

print("O break quebrou o 'else'.")