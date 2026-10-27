#Exercício 03
#Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês
ganho_horas = float(input('Quantas você ganha por hora trabalhada: '))
horas_trabalhadas = int(input('Digite o número de horas trabalhada: '))

#Calculo do salario
salario = ganho_horas * horas_trabalhadas

#mostrar o resultado
print(f'O total do meu salario no mês é: R$ {salario:.2f}')

