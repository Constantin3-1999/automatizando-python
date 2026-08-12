"""while/else"""
string = 'VIDAEUTEAMO' 

i = 0 #variavel i para contar indices 
while i < len(string): #checando se indice e maior que string
    letra = string[i] #pegando cada eltra 
    
    if letra == ' ':
        break

    print(letra) #imprimi cada letra na tela
    i += 1 #somando + 1 no indice

else: #executado fora do while 
    print('Não encontrei espaço na string.') #fora do while
print('Fora do while.')