"""chuva = input("Está chovendo? ")

if chuva == 'sim':
    print("Abrir o guarda chuva")

else:
    print("Não precisa abrir o guarda chuva")"""

"""nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nome = input("Digite o nome do aluno: ")

media = (nota_1 + nota_2) / 2

print(nome, nota_1, nota_2, media)

if media < 6:
    print("Aluno reprovado!!")

else:
    print("Aluno aprovado!!")"""


"""chuva = input("Está chovendo? ")

if chuva == 'sim':
    print("Ver televisão em casa")

else:
    print("Passear no parque")"""



"""estado_civil = int(input("Digite 1 se for solteiro, digite 2 se for casado: "))
if estado_civil == 1:
    print("Solteiro")

elif estado_civil == 2:
    print("Casado")

else:
    print("Outros")"""

"""estacao = input("Escreva a aestação do ano: ")

if estacao == 'verão':
    print("Cuidado com o sol!")
elif estacao == 'inverno':
    print("Se agasalhe bem!")
elif estacao == 'primavera':
    print("Aprecie seu jardim!")
elif estacao == 'outono':
    print("Passei no bosque!")
else:
    print("Até a proxima!")"""

import turtle 

window = turtle.Screen()
window.bgcolor("pink")
window.title("EU TE AMO")

pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.pensize(3)
pen.speed(7)

pen.begin_fill()
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

pen.up()
pen.goto(0, -70)
pen.down()
pen.color("black")

pen.hideturtle()

turtle.done()