def multiplos_de_i_ou_j(n, i, j):
    resultado = []
    x = 0 
    while len(resultado) < n:
        if x % i == 0 or x % j == 0:
            resultado.append(x)

        x += 1
    return resultado

n = int(input('Entre com o valor de n: '))
i = int(input("Entre com o valor de i: "))
j = int(input("Entre com o valor j: "))

resultado = multiplos_de_i_ou_j(n, i, j)
print(resultado)