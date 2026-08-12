
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

def encontre_estacao(dia, mes):
    if (mes == 3 and dia >= 20) or (mes > 3 and mes <6):
        return "Primavera"
    elif (mes == 6 and dia >= 20) or (mes >6 and mes <9):
        return "Verão"
    elif (mes == 9 and dia >= 22) or (mes > 9 and mes < 12):
        return "Outono"
    elif (mes == 12 and dia >= 21) or (mes > 12) or (mes < 3):
        return "Inverno"

    estacao = encontre_estacao
    print("A data cai na: ", estacao)