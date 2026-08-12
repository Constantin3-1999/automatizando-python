#Exercícios 
#Crie funções que duplicam, triplicam e quadruplicam
#o numero recebido como parâmetro

#def duplicar(numero):
#    return numero * 2


#def triplicar(numero):
#    return numero * 3


#def quadruplicar(numero):
#    return numero * 4


#print(duplicar(2))
#print(triplicar(2))
#print(quadruplicar(2))

def cria_multplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = cria_multplicador(2)
triplicar = cria_multplicador(3)
quadruplicar = cria_multplicador(4)


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))