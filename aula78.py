# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}


#s1 = set() #vazio
#s1 = {'Victor', 1, 2, 3} #com dados




# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

#s1 = set('Victor')
#print(s1)



# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Victor')
s1.update('1, 2, 3')
#s1.clear()
s1.discard('Victor')
#print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3_1 = s1 | s2
s3_2 = s1 & s2
s3_4 = s2 - s1
s3_5 = s1 ^ s2
print(s3_1)
print(s3_2)
print(s3_4)
print(s3_5)