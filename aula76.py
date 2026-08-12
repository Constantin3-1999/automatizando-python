# Diconários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor"
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tu´le, etc.
# O valor pode ser de qualquer tipó, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
#pessoa = {
#    'nome': 'João Victor',
#    'sobrenome': 'Freitas',
#    'idade': 27,
#    'altura': 1.7,
#    'endereços': [
#        {'rua': 'Pessegueiros', 'número': 184},
#    ]
#}
#print(pessoa, type(pessoa))
#pessoa = dict(nome='João Victor', sobrenome='Freitas')

pessoa = {
    'nome': 'João Victor',
    'sobrenome': 'Freitas',
    'idade': 27,
    'altura': 1.7,
    'endereços': [
        {'rua': 'Pessegueiros', 'numero': 184},
        {'Rua': 'Garcia Lorca', 'numero': 380},


    ],
}
#pessoa = di₢ct(nome='João Victor', sobrenome='Freitas')

#print(pessoa, type(pessoa))