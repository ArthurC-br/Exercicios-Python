"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
para cada jogo, cadastrando tudo em uma lista composta.
"""

listNotas = list()
while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2

    listNotas.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N] "))
    if resp in "nN":
        break
        
print("====" * 10)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print("---" * 10)

for i, n in enumerate(listNotas):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8.1f}')

while True:
    print("---" * 10)
    opc = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opc == 999:
        print("Finalizando...")
        break
    if opc <= len(listNotas) -1:
        print(f"Notas de {listNotas[opc][0]} são {listNotas[opc][1]}")
print("Volte sempre")