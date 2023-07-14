frase = 'O Python é uma linguagem de programção multiparadigma. Python foi criado por Guido Van Rossum.'

i = 0

qtd_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    
    qts_apareceu = frase.count(letra_atual)
    #print(letra_atual, qts_apareceu)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_mais_vezes < qts_apareceu:
        qtd_mais_vezes = qts_apareceu
        letra_mais_vezes = letra_atual
    
    i += 1 
    
print('O elemento que mais apareceu'
      f' foi "{letra_mais_vezes}", repetido: {qtd_mais_vezes}x.')