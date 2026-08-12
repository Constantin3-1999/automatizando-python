from datetime import datetime

def calcular_media_tempo_producao(registros):
    total_tempo = 0
    total_registros = len(registros)

    for registro in registros:
        inicio = datetime.strptime(registro['inicio'], '%H:%M')
        fim = datetime.strptime(registro['fim'], '%H:%M')
        tempo_producao = fim - inicio
        total_tempo += tempo_producao.total_seconds()

    media_tempo = total_tempo / total_registros
    return media_tempo

def coletar_registro():
    registro = {}
    inicio = input("Digite o horário de início da produção (HH:MM): ")
    fim = input("Digite o horário de término da produção (HH:MM): ")
    registro['inicio'] = inicio
    registro['fim'] = fim
    return registro

def main():
    registros = []
    continuar = True

    while continuar:
        registro = coletar_registro()
        registros.append(registro)

        resposta = input("Deseja registrar mais um período de produção? (s/n): ")
        if resposta.lower() != 's':
            continuar = False

    media_tempo_producao = calcular_media_tempo_producao(registros)
    print("A média de tempo para produzir é de:", media_tempo_producao, "segundos.")

if __name__ == '__main__':
    main()
