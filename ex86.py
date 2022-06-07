"""
Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for n in range(0,3):
        matriz[i][n] = int(input(f"Digite o valor da [{i}, {n}]: "))

print("===="*10)
for i in range(0, 3):
    for n in range(0,3):
        print(f"[{matriz[i][n]:^5}]", end="")
    print()
