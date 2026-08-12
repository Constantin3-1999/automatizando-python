"""
Imprecisão de ponto flutuante
Double-precision floeting-point format IEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}') #():.2f) e possivel arredondar o número
print((round(numero_3, 3))) 
