"""
Exercício 17

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer 
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele 
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
    ...
5 X 10 = 50
"""
def tabuada(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')

n = int(input('Digite o numero da tabuada que deseja saber(1 a 10): '))
if 1 <= n <= 10:
    print(f'Tabuada de {n}: ')
    tabuada(n)
else:
    print('Numero invalido! somente entre 1 e 10')
    