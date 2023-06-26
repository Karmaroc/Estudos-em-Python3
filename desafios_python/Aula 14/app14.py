def valor():
    
    atual = 1
    valor = 1
    numero = 6
    
    while (atual <= numero):
        valor = valor * atual
        atual = atual + 1
        
        print("Digito atual:", atual, "valor:", valor)
        
    
valor()

print("================================")

def letra():
    
    m = 20
    n = 15
    
    i = 0
    
    while (i < 10):
        i = i + 1
        
        m = m - 1
        n = n + 1
        
        print(m, " ",n, " ")
        
letra()
        
        