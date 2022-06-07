"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
listNum = []
while 1:
    aux = int(input("Digite um numero: "))
    if not aux in listNum:
        listNum.append(aux)
    else:
        print(f"{aux} ja existe na lista! Nao vou adicionar")

    if input("Voce deseja continuar?[S/N] ") in "sS":
        pass
    else:
        break
listNum.sort()
print(f"Os valores adicionados foram {listNum}")