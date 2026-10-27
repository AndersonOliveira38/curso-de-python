#Exercício 05
#Tendo como dado de entrada a altura (h) de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#   Para homens: (72.7h) - 58
#   Para mulheres: (62.1h) - 44.7

sexo = input('Digite [h] para homem ou [m] para mulher: ').strip().lower()

if sexo in ('h', 'homem'):
    altura = float(input('Digite sua altura em metros (ex.: 1.75): '))
    peso_ideal = (72.7 * altura) - 58
    print(f'Seu peso ideal é: {peso_ideal:.2f} kg')
elif sexo in ('m', 'mulher'):
    altura = float(input('Digite sua altura em metros (ex.: 1.75): '))
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é: {peso_ideal:.2f} kg')
else:
    print('Opção inválida. Digite h ou m.')
