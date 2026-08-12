from datetime import date
import datetime

namoro = datetime.datetime(2022, 8, 14, 20, 45)

hoje = datetime.datetime.now()

diferenca = hoje - namoro 
print(f'Seu aniversário de namoro e daqui {diferenca}')