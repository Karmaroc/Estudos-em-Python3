"""isupper e islower - Tudo maisculo e tudo minusculo
- strip()
"""

minha_string = "qualquer texto t t t"

print(type(minha_string)) 

print(f'{minha_string} é o suficiente.')

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.isupper())
print(minha_string.islower())
print(minha_string.strip())
print(minha_string.replace("t", "T", 4))

string = "Vitor Manoel"

print(len(string))
print(string[1:5])
print(string[-4:-1])
print(string.index('M'))

x = 'Vitor' in string
print(x)


palavras = """linha 1, \nlinha 2, \nlinha 3."""
print(palavras)

aspas = "Programação é \"legal\"."
print(aspas)

