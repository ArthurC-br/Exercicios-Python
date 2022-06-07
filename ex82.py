"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

numList = []
while 1:
    numList.append(int(input("Digite um numero: ")))
    if input("Voce deseja continuar?[S/N] ") in "sS":
        pass
    else:
        break

print(f"A lista completa é {numList}")
numListPar = []
numListimpar = []

for i in numList:
    if i % 2 ==0:
        numListPar.append(i)
    else:
        numListimpar.append(i)
print(f"A lista de pares é {numListPar}")
print(f"A lista de impares é {numListimpar}")
