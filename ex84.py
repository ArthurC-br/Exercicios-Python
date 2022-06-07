"""
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
"""

nomeList = []
pesoList = []
nomesMais = []
nomesMenos = []
while 1:
    nomeList.append(str(input("Nome: ")))
    pesoList.append(float(input("Peso: ")))
    if input("Voce deseja continuar?[S/N] ") in "sS":
        pass
    else:
        break
aux = 0 #maior
aux2 = 0 #menor
for i in range(0, len(pesoList)):
    if pesoList[i] > pesoList[i-1]:
        aux = pesoList[i]
        continue
    elif pesoList[i] < pesoList[i-1]:
        aux2 = pesoList[i]
        continue

n = 0
k = 0
for i in pesoList:
    if i == aux:
        nomesMais.append(nomeList[pesoList.index(i+n)])
        n += 1
    if i == aux2:
        nomesMenos.append(nomeList[pesoList.index((i+k))])
        k += 1

print(f"O maior peso foi de {aux}Kg. Peso de {nomesMais}")
print(f"O menor peso for de {aux2}Kg. Peso de {nomesMenos}")
