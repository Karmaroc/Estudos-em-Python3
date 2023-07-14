linhas = 5
linha = 1 

while linha <= linhas:
    
    if linha == 1:
        coluna = 2
        coluna2 = coluna + 1
        coluna3 = coluna2 + 1
        coluna4 = coluna3 + 1
        
        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    elif linha == 2:
        coluna = 3
        coluna2 = coluna + 1
        coluna3 = coluna2 + 1
        coluna4 = coluna3 + 1
        
        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    elif linha == 3:
        coluna = 4
        coluna2 = coluna + 1
        coluna3 = coluna2 + 1
        coluna4 = coluna3 + 1

        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    elif linha == 4:
        coluna = 5
        coluna2 = coluna + 1
        coluna3 = coluna2 + 1
        coluna4 = coluna3 + 1
        
        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    elif linha == 5:
        coluna = 6
        coluna2 = coluna + 1
        coluna3 = coluna2 + 1
        coluna4 = coluna3 + 1
        
        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    
    else:
        print(f'{linha} | {coluna} | {coluna2} | {coluna3} | {coluna4}')
    linha += 1    
    
    
i = 0
while i < 5:
    i += 1
    contador = 0
    
    while contador < 5:
        contador += 1
    print(f'{i} = {contador}')