'''
Extra 01

Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de 
cada candidato.

'''
eleitores = int(input('Numero total de eleitores: '))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(eleitores):
    voto = int(input('Candidatos 1,2 ou 3: '))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print('voto invalido')

print(f'Votos do candidato 1: {candidato1}')
print(f'Votos do candidato 2: {candidato2}')
print(f'Votos do candidato 3: {candidato3}')
print(f'Total de votos: {candidato1 + candidato2 + candidato3}')
