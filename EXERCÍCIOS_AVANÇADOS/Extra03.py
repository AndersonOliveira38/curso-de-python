'''
Certo Hipermercado está com uma promoção de carnes que é imperdível. Confira:

Produto        |   Até 5 Kg       |   Acima de 5 Kg
File Duplo     |   R$ 12,00 por Kg |   R$ 14,90 por Kg
Alcatra        |   R$ 25,00 por Kg |   R$ 29,99 por Kg
Picanha        |   R$ 40,00 por Kg |   R$ 49,99 por Kg


Não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto 
de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo 
usuário e gere um cupom fiscal, contendo as informações da compra: 
tipo e quantidade de carne, 
preço total, 
tipo de pagamento, 
valor do desconto e valor a pagar.
'''
file_duplo = 'file duplo'
alcatra = 'alcatra'
picanha = 'picanha'

def calcular_preco(tipo, quantidade):
    if tipo == file_duplo:
        if quantidade <= 5:
            return quantidade * 12.00
        else:
            return quantidade * 14.90
    elif tipo == alcatra:
        if quantidade <= 5:
            return quantidade * 25.00
        else: 
            return quantidade * 29.99
    elif tipo == picanha:
        if quantidade <= 5:
            return quantidade * 40.00
        else:
            return quantidade * 49.99

print('Tipos de carne: File Duplo, Alcatra, Picanha')
tipo = input('Digite o tipo desejado: ').lower()
quantidade = float(input('kg de carne: '))
preco_total = calcular_preco(tipo, quantidade)
print(f'Preço total: R$ {preco_total:.2f}')

pagamento = input('Forma de pagamento (dinheiro ou cartão): ').lower()
if pagamento == 'cartão':
    desconto = preco_total * 0.05
    preco_final = preco_total - desconto
    print(f'Desconto:R$ {desconto:.2f}')
else:
    desconto = 0
    preco_final = preco_total

print(f'Valor pago: R$ {preco_final:.2f}')