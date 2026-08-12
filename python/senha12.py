import random

lower_case = "abcdfghijklmnopqrsuvwxyz"
upper_case = "ABCDFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%¨&*()=-+;~][`^:?/|]"

for_pass = lower_case + upper_case + number + symbols

tamanho_da_senha = 12

password = "".join(random.sample(for_pass, tamanho_da_senha))

print("Minha senha: ", password)