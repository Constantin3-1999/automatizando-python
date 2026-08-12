"""
Lista de listas e seus indices
"""

salas = [ 
    # 0        1 
    ['Maria', 'Helena',],   #0
    # 0
    ['Elaine', ],  #1
    # 0       1      2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)],  

]

print(salas[1][0])
print(salas[0][1])
print(salas[2][2]) # para buscar usar o valor da lista e o valor que esta dentro da lista
print(salas[2][3][2]) # aqui o pai desenrolou

# for sala in salas:
#    print(f'A sala é {sala}')
#    for aluno in sala:
#        print(aluno)