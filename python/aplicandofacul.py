
idade = int(input("Digite a idade do atleta: "))


if idade < 5:
    categoria = "Não tem idade para ser atleta"
elif 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Sênior"

print(f"A categoria do atleta é: {categoria}")