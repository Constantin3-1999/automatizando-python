"""
iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
#for letra in texto

texto = 'João' #iteravel 
#iterador = iter(texto) #iterator

#while True:
#    try:
#        letra = next(iterador)
#        print(letra)
#    except StopIteration:
#        break

#O de baixo faz a mesma bosta so que mais rapido
for letra in texto:
    print(letra)
