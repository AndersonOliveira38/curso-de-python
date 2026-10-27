#    Tamanho de strings. Faça um programa que leia 2 strings e informe o 
# conteúdo delas seguido do seu comprimento. Informe também se as duas strings 
# possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
#Modelo:
#String 1: Brasil Hexa 2006
#String 2: Brasil! Hexa 2006!
#Tamanho de "Brasil Hexa 2006": 16 caracteres
#Tamanho de "Brasil! Hexa 2006!": 18 caracteres
#As duas strings são de tamanhos diferentes.
#As duas strings possuem conteúdo diferente.

''' Informando a string'''
string_1 = input('digite uma frase: ')
string_2 = input('digite outra frase: ')

''' Vendo a string 1 e 2'''
print(f'Frase 1:{string_1} ')
print(f'A frase 2:{string_2}')

'''Verificando o tamanho das strings'''
print(f'O tamanho da "{string_1}": {len(string_1)} caracteres')
print(f'O tamanho da "{string_2}": {len(string_2)} caracteres')

''' Verificando o tamanho'''
if len(string_1) == len(string_2):
    print(f'As duas strings são de tamanhos identicos.')
else:
    print(f'O tamanho é diferente')

'''Verificando se o conteudo são iguais'''
if string_1 == string_2:
    print("O conteúdo das frases são iguais.")
else:
    print("O conteúdo é diferente")





