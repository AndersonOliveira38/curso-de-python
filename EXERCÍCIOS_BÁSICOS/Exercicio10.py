#Exercício 10
#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido.

nota = float(input('Informe um numero de 0 a 10: '))

# O while já funciona como uma condição, não precisa de if/else aqui dentro
while nota < 0 or nota > 10:
    print('Valor invalido!')
    nota = float(input('Informe uma nota de 0 a 10 valida: '))

print(f'Nota {nota} registrada com sucesso')

