from random import randint
""" Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
    Depois disso, mostre a listagem de números gerados e também indique o menor e o 
    maior valor que estão na tupla. """

num_rand = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))

print(f'Os numeros gerados foram: ', end='')
for i in num_rand:
    print(f' {i}', end='')

print(f'\nMenor valor é: {min(num_rand)}')
print(f'Maior valor é:', max(num_rand))