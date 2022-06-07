
"""
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Chapecoense.
"""


t_brasil = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
    'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
    'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
    'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

print(t_brasil)
print('===='*10)

print('Os 5 primeiros times.')
print(t_brasil[0:5])
print('===='*10)

print('Os últimos 4 colocados.')
print(t_brasil[len(t_brasil)-4:])
print('===='*10)

print('Times em ordem alfabética.')
print(sorted(t_brasil))
print('===='*10)

print('Em que posição está o time da Chapecoense.')
print(t_brasil.index('Chapecoense'))

