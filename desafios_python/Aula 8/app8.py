i = 0

while i <= 10:
    print(i)
    i = i + 1
    
print("i =", i)

kid = ["Deméter", "Khaelum", "Karmaroc", "Khaylesti"]

for item in kid:
    print(item)
    

nome = "Manoel"

for letra in nome:
    print(letra)   

for index in range(2, 20):
    print(index)
    
for index in range(5, 21, 2):
    print(index)
    
for index in range(len(kid)):
    print(kid[index], index)
    
for index in range(5):
    if index == 0:
        print("primeira linha")
    else:
        print(f'outras linhas {index}')
        
matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for elemento in matriz_numeros:
    print(elemento)
    for coluna in elemento:
        print(coluna)    
    