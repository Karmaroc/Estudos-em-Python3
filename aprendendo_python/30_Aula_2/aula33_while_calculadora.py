sair_entrar = 'r'

while sair_entrar != "s" and sair_entrar == 'r': 

    numero1 = input("Digite um número: ")
    operador = input("Digite um operador [+, -, *, /]: ")
    numero2 = input("Digite um segundo número: ")
    
    if not numero1.isdigit():
        print('Não é um número a primeira opção.')

    elif not numero2.isdigit():
        print('Não é um número a segunda opção.')

    elif not numero1.isdigit() and not numero2.isdigit():
        print('A primeira e segunda opção não foram digitadas.')
        
    elif operador == "+":
        soma = int(numero1) + int(numero2)
        print(f'Resultado: {soma}')
        
    elif operador == "-":
        if numero1 >= numero2:
            sub = int(numero1) - int(numero2)
            print(f'Resultado: {sub}')
            
        elif numero2 > numero1:
            sub = int(numero1) - int(numero2)
            print(f'Resultado: {sub:-}')

    elif operador == "*":
        mul = int(numero1) * int(numero2)
        print(f'Resultado: {mul}')

    elif operador == "/":
        div = float(numero1) / float(numero2)
        print(f'Resultado: {div:.2f}')
        
    else:
        if (operador not in ["+", "-", "*", "/"]):
            print("Não é um operador válido.")

    sair_entrar = input("Digite '[s]air' ou '[r]epetir' na Calculadora: ")
        
