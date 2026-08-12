"""
Ex.3
Um banco concederá um crédito especial a seus clientes de acordo com o saldo médio 
no último ano. Faça um pseudocódigo que receba o saldo médio de um cliente e calcule o valor
do crédito, de acordo com a tabela a seguir. Mostre o saldo médio e o valor do crédito.

Saldo Médio                     | Percentual 
Até R$ 200,00                   | 10% do saldo médio
Entre R$ 200.01 e R$ 300,00     | 20% do saldo médio
Entre R$ 300,01 e R$ 400,00     | 25% do saldo médio
Acima de R$ 400,00              | 30% do saldo médio
"""

saldomedio = float(input('Digite o saldo: '))
if saldomedio <= 200:
    credito = saldomedio * 0.1
elif saldomedio <= 300:
    credito = saldomedio * 0.2
elif saldomedio <= 400:
    credito = saldomedio * 0.25
else: 
    credito = saldomedio * 0.3
print(f'Valor do crédito é (credito)') 