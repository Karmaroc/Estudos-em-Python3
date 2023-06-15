try:
    numero = int(input("Digite um número: "))
    print(numero)
    print(x)

    valor = numero / 0
    
except ZeroDivisionError: #Except é um erro, so entra por cauda disso.
    print("Dividir por zero não é possível.") 

except ValueError:
    print("Digite um valor válido.")
         
except:
    print("Erro Inesperado.")
    
finally: 
    print("Sempre Executa.")
    

    
