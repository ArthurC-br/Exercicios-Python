"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
numList = []
while 1:
    numList.append(int(input("Digite um numero: ")))
    if input("Voce deseja continuar?[S/N] ") in "sS":
        pass
    else:
        break

numList.sort()
numList.reverse()

print(f"Voce digitou {len(numList)} elementos")
print(f"Os valores em ordem decrescente são {numList}")
if numList.count(5) != 0:
    print("O valor 5 foi encontrado na lista")
else:
    print("O valor 5 nao foi encontrado na lista")


