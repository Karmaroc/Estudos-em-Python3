"""
Qual o elemento e a quantidade de vezes que menos se repete.
"""

from collections import Counter

lista = [1, 1, 2, 2, 2, 2, 2, 3, 4, 4, 5, 5, 6, 6, 6, 'a',
        'a', 'a', 'a', 'b', 'b', 'c', 'c'
        ]

repete = Counter(lista).most_common()
print(repete[-1])
