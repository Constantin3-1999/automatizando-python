frase = 'aaaooo'

i = 0 #indice 
apareceu_mais_vezes = 0 
letra_aparece_mais_vezes = ''

while i < len(frase): #saber qual letra apareceu mais
    letra_atual = frase[i] #indice 0 onde coemeça a string

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_aparaceu_atual = frase.count(letra_atual)
    
    
    if apareceu_mais_vezes <= quantas_vezes_letra_aparaceu_atual:
       apareceu_mais_vezes = quantas_vezes_letra_aparaceu_atual
       letra_aparece_mais_vezes = quantas_vezes_letra_aparaceu_atual
    
    i += 1

print('A letra que apareceu mais vezes foi '
f'{letra_aparece_mais_vezes} que apareceu '
f'{apareceu_mais_vezes}x')