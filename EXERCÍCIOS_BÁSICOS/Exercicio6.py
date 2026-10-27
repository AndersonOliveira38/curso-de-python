#Exercício 06
#Faça um Programa que peça dois números e imprima o maior deles.

num_1 = int(input('Digite um numero: '))
num_2 = int(input('Digite outro numero: '))

if num_1 > num_2:
    print(f'O numero maior é: {num_1}')

elif num_2 > num_1:
    print(f'O numero maior é: {num_2}')

else: 
    print('Os dois numeros são iguais.')