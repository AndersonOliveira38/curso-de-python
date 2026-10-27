#Exercício 14
#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
#F
#U
#L
#A
#N
#O

''' Pedir que digite um nome'''
nome = input('Digite o nome: ')

''' Percorrer o nome com "for" e devolver ele na vertical'''
for letra in nome:
    print(f'{letra}')

