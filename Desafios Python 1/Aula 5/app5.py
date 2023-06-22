familia = ['Vitor', 'Dri', 'Ehza', 'Khaelum']

print(familia[0])
print(familia[-1])

print(familia[2:1])

familia[1] = 'Primavera'

print(familia)

familia.extend(["Fernando", "Dri"])

print(familia)

familia.append("Spock")

print(familia)

familia.pop()

print(familia)

familia.remove("Vitor")

print(familia)

#familia.clear()

print(familia)

print(familia.index("Dri"))

idade_familia = [23, 35, 57, 78, 9]
print(idade_familia)

idade_familia.sort() # Ordena em ordem crescente 

print(idade_familia)

idade_familia.reverse() # Reverte a lista

print(idade_familia)

familia.remove("Ehza")
print(familia)

familia2 = familia.copy()
print(familia2)

coordenadas = [-45, -3]
coordenadas.pop()

print(coordenadas)
