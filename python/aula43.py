#Laço de repetição for / in

#senha_salva = '147852369'
#senha_digitada = ''
#repeticoes = 0 

#while senha_salva != senha_digitada:
#    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#    repeticoes += 1

#print(repeticoes)
#print('Aquele laço acima pode ter repetições infinitas')

texto = 'João gato'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')