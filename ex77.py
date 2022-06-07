"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')
aux = ''

for i in palavras:
    for n in i:
        if n in vogais:
            aux += " " + n
    print(f"A palavra {i.upper()} tem as vogais: {aux}")
    aux = ''
