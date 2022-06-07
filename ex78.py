"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""

listNum = []
for i in range(0, 5):
    listNum.append(int(input(f"Digite um valor para a pos {i}: ")))

print(listNum)
print(f"Maior valor: {max(listNum)} no index: {listNum.index(max(listNum))}")
print(f"Menor valor: {min(listNum)} no index: {listNum.index((min(listNum)))}")


