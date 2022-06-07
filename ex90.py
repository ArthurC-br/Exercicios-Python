"""
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela.
"""

aluno = dict()

aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Média de {aluno['nome']}: "))
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif aluno["media"] <=5:
    aluno["situação"] = "Reprovado"
else:
    aluno["situação"] = "Recuperacao"

print("===" * 10)

print("Nome é igual a ", aluno["nome"])
print("Média é igual a ", aluno["media"])
print("Situacao é igual a ", aluno["situação"])
