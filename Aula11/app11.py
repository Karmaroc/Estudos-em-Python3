#open("caminho", "r")

# Mode
# r - Leitura
# a - Append / Incrementar
# w - Escrita
# x - Criar arquivo
# r+ - Leitura + Escrita

#arquivo = open("Aula11/test2.txt", "x")

#print(arquivo.readable())
#print(arquivo.read())

#print(arquivo.readline())
#print(arquivo.readline())

#list = arquivo.readlines()
#print(list)
#print(list[3])

#arquivo.write("Vitor")
#arquivo.write("\nManoel")
#arquivo.write("\nDe Paula")
#arquivo.write("\nVieira")

#arquivo.close()

import os

if os.path.exists("Aula11/test2.txt"):
    os.remove("Aula11/test2.txt")
else:
    print("Arquivo não existe")
    
#os.rmdir() remove pasta vazia.