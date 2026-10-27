#Exercício 12
#Faça um programa que peça um número inteiro e determine se ele é ou não um 
# número primo. Um número primo é aquele que é divisível somente por ele mesmo 
# e por 1.

''' Digite o numero'''

numero = int(input('digite um numero: '))

''' Variável para contar quantos divisores o numero possui'''
total_divisores = 0

''' Testamos a divisão do número por todos os valores
de 1 até ele'''
for i in range(1, numero + 1):
    if numero % i == 0:
        total_divisores += 1

''' Um número primo so pode ser divido por 1 e por ele mesmo'''
if total_divisores == 2:
    print(f'O numero {numero} é PRIMO!!')
else:
    print(f'O número {numero} NÃO É PRIMO!!')
