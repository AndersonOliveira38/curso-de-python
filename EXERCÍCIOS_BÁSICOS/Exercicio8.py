#Exercício 08
#Determinada empresa resolveu dar um aumento de salário aos seus colaboradores 
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador. 
# Os critérios para reajuste são:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

#Qual é o salario atual do funcionario:
salario_atual = float(input('Digite o seu salario atual: R$ '))

#Determinar a porcentagem de aumento no salario atual:
if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

#calculo do novo salario
salario_novo = salario_atual * (percentual / 100)
novo_salario = salario_atual + salario_novo

#Exibição dos resultados
print(f'\nSalário antes do reajuste: R$ {salario_atual:.2f}')
print(f'Percentual de aumento no salario novo: {percentual} %')
print(f'Valor do aumento: R$ {salario_novo:.2f}')
print(f'Novo salario, apos o aumento: R$ {novo_salario:.2f}')


