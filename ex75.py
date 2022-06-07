"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

num = (int(input("Digite um numero: ")),
       int(input("Digite outro numero: ")),
       int(input("Digite outro numero: ")),
       int(input("Digite outro numero: "))
       )
print('Quantas vezes apareceu o valor 9.')
print(num.count(9))
print("===="*10)

print('Em que posição foi digitado o primeiro valor 3.')
print(num.index(3))
print("===="*10)

print('Quais foram os números pares.')
n = 0
for i in num:
    if i % 2 == 0:
        n += 1
        print(i)

if n == 0:
    print('Nenhum numero par.')
