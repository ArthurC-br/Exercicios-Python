"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""

listNum = []
for i in range(0,5):
    aux = int(input("Digite um numero: "))
    if i == 0 or i > listNum[-1]:
        listNum.append(aux)
    else:
        for n in range(0, len(listNum)):
            if aux <= listNum[n]:
                listNum.insert(n, aux)

print("===="*10)
print(f"Os valores digitados foram: {listNum}")
