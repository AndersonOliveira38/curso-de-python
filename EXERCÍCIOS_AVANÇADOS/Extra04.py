'''
Extra 04

O Sr. Benedito Pires comprou uma loja de conveniências. 

p1 = Faça um programa que implemente uma caixa registradora rudimentar. 

p2 =O programa deverá receber um número desconhecido de valores referentes aos 
preços das mercadorias. 

p3 = Um valor zero deve ser informado pelo operador para indicar o final da compra. 

p4 = O programa deve então mostrar o total da compra e perguntar o valor em 
dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 

p5 = Após esta operação, o programa deverá voltar ao ponto inicial, para 
registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00

'''
caixa_registradora = True
while caixa_registradora:
    print('Lojas Tabajara')
    i = 1
    valores = []
    while True:
        valor = float(input(f'Produto {i}: R$ '))
        if valor == 0:
            break

        valores.append(valor)
        i += 1

    total = sum(valores)
    print(f'Total: R$ {total:.2f}')
    dinheiro = float(input('Dinheiro: R$ '))
    troco = dinheiro - total
    print(f'Troco: R$ {troco:.2f}')

