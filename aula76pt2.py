# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'João Victor'
pessoa['sobrenome'] = 'Freitas'

print(pessoa[chave])

pessoa[chave] = 'Maria'

#del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print(pessoa['sobrenome'] )

if pessoa.get('sobrenome') is None:
    print('Não EXISTE')
else:
    print(pessoa['sobrenome'])

#print('isso não vai ')