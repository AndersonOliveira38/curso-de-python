#Exercício 04
#Tendo como dados de entrada a altura de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58

#Entrada pedindo a altura
altura = float(input('Digite a sua altura: '))

#calculo do peso ideal
peso_ideal = (72.7 * altura) - 58

#Resultado do calculo
print(f'Seu peso ideal é : {peso_ideal:.2f} quilos')
