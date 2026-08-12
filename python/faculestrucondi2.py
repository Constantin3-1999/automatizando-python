"""
Ex.2
Elabore um programa que calcule e mostre o valor que deve ser pago por um produto, 
considerando que o usuário fornecerá o preço normal de etiqueta e o código da condição
de pagamento. 
Utilize os códigos da tabela seguinte para ler qual é a condição de pagamento escolhida e efetuar o cálculo
adequado.

Código            |Condições de pagamento
1                 |À vista em dinheiro ou débito, recebe 10% de desconto.
2                 !À vista no cartão de crédito, recebe 5% de desconto. 
3                 !Em 2 vezes, preço normal de etiqueta sem juros. 
4                 !Em 3 vezes, preço normal de etiqueta mais juros de 10%. 
"""
preco = float(input('Preço normal da etiqueta: '))
cod = int(input('Código (1 a 4:)'))
if cod == 1:
    valor = preco * 0.90
    print("À vista em dinheiro ou débito, recebe 10%% de desconto: R$ %.2f " %valor)
elif cod == 2:
    valor = preco * 0.95
    print('À vista no cartão de credito, recebe 5%% de desconto: R$ %.2f ' %valor)
elif cod == 3:
    valor =  preco / 2 
    print('Em 2 vezes, preço normal de etiqueta sem juros. \nValor da parcela: R$ %.2f ' %valor)
elif cod == 4:
    valor = preco / 3
    print('Em 3 vezes, preço normal d etiqueta mais juros de 10%%. \nValor da parcela: R$ %.2f ' %valor)
else:
    print('Código invalido')