'''
Exercício 16

Faça um Programa que peça dois números inteiros e imprima o maior deles. 
Criar funções para manter o código organizado.
'''
def maior(f, d):
    if f > d:
        return f
    else: 
        return d

f = int(input('numero 1: '))
d = int(input('numero 2: '))
print(f'O maior é {maior(f, d)}')
