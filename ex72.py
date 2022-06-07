### ler numero do teclado e mostrá-lo por extenso


num = ('zero', 'um', 'dois', 'tres', 'quatro','cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte'
       )
while 1:
    op = int(input("Digite um numero de 0 a 20: "))
    if 0 <= op <= 20:
        print(num[op])
    else:
        print("Digite um numero valido")
