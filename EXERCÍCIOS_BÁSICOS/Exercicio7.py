#Exercício 07
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

#lendo os numeros
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
n3 = int(input('Digite outro numero: '))

if n1 >= n2 and n2 >= n3:
    maior = n1
    if n2 >= n3:
        medio, menor = n2, n3
    else:
        medio, menor = n3, n2

elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 >= n3:
        medio, menor = n1, n3
    else:
        medio, menor = n3, n1
else:
    maior = n3
    if n1 >= n2:
        medio, menor = n1, n2
    else:
        medio, menor = n2, n1

print(f'A ordem decrescente: {maior}, {medio},{menor}')

