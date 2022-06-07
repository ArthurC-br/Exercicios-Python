"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

listNum = [[], []]


for i in range(1,8):
    num = int(input(f"Digite o {i}o. Valor: "))
    if num%2 ==0:
        listNum[0].append(num)
    else:
        listNum[1].append(num)

listNum[0].sort()
listNum[1].sort()
print(f"Os valores pares digitados foram: {listNum[0]}")
print(f"Os valores impares digitados foram: {listNum[1]}")

