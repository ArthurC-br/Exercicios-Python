from random import randint
from time import sleep
"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""


listNum = []

aux = int(input("Quantos jogos voce deseja sortear? "))
aux2 = 0
while aux2 != aux:
    for i in range(0,6):
        num = randint(1, 60)
        if num not in listNum:
            listNum.append(num)

    aux2+=1
    listNum.sort()
    print(f"O jogo {aux2}: {listNum}")
    listNum.clear()
    sleep(1)



