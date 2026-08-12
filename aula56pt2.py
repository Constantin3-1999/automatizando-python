"""
split e join com list e str
split - divide uma string (list) #também retorna uma lista
join - une uma string
"""

frase = '     Olha só que     , coisa interessante     '
lista_frases_cruas = frase.split(',') #adicione a variavel antes de .spli ou . join

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = '-'.join(lista_frases) # oque e colocado entre '' e adicionado a frase ou lista e tuplas
print(frases_unidas)