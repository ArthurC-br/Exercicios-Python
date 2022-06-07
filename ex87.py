"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
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

print("===="*10)

somaPar = 0
somaCol = 0
tempMax = 0
for i in range(0, 3):
    for n in range(0,3):
        if matriz[i][n]%2 == 0:
            somaPar += matriz[i][n]
        if n == 2:
            somaCol += matriz[i][2]
        if i == 1:
            if matriz[1][n] > tempMax:
                tempMax = matriz[1][n]

print(f"A soma dos valores pares é {somaPar}")
print(f"A soma dos valores da terceira coluna é {somaCol}")
print(f"O maior valor da segunda linha é {tempMax}")



