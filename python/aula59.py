# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

# p, b, *_, u  = lista
# print(p, *_) # *_ serve para os inteiros dentro da lista

# for vitor in lista:
#    print(vitor, end=' ') #Assim funciona um desenpacotamento em funções

# print(*lista) # mesma coisa que o de cima 
# print(*string) # '*' passa cada lista uma por uma 
# print(*tupla)

print(*lista, sep='')