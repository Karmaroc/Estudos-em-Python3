#def big_mac():
#    print("Sanduiche big mac")

#print("Inicio")
#big_mac()   
#print("FIM")

def fazer_big_mac(nome):
    print(f'Sanduiche big mac para {nome}')

#fazer_big_mac("Vitor")
#fazer_big_mac(10)
#fazer_big_mac("Manu")

def fazer_batata(tamanho):
    print(f'batata {tamanho}')
    
def preparar_refrigerante(tipo, tamanho):
    print(f'{tipo} {tamanho}')
    
#fazer_batata("Grande")
#preparar_refrigerante("Coca", "Grande")

def fazer_combo_big_mac(nome, batata, refri, tamanho):
    fazer_big_mac(nome)
    fazer_batata(batata)
    preparar_refrigerante(refri, tamanho)

fazer_combo_big_mac("Vitor", "Grande", "Fanta", "Médio") 


def soma_num(num1, num2):
    return num1 + num2

resultado = soma_num(15, 15)

print(resultado)

def maior_num(lista):
    return max(lista)

maior = maior_num([10, 5, 11, 22])

print(maior) 
   