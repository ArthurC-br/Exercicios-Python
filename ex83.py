"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

expressao = input("Digite uma expressão: ")

n = 0
for i in expressao:
    if i == '(':
        n+=1
    if i == ')':
        n-=1

if n==0:
    print("Sua expressao esta correta")
else:
    print("Sua expressao esta incorreta")