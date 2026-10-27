'''
Extra 05
Faça um programa para imprimir:

    1
    1 2
    1 2 3
    .....
    1 2 3 ... n

'''

def imprimir(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

n = int(input('Digite o 1º numero: '))
imprimir(n)

