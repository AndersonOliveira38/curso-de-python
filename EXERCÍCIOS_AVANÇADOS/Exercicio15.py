'''
Exercício 15

Faça um Programa que peça dois números inteiros e imprima a soma. 
Criar funções para manter o código organizado
'''

def soma(n1, n2):
    return n1 + n2

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print(f'Somando {n1} + {n2} = {soma(n1, n2)}')
