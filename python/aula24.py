nome = input('Digite um nome: ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else: 
    print(f'{encontrar} não está em {nome}')