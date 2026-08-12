from pprint import pprint


def encontre_proximo_vazio(puzzle):
    # encontra a próxima linha \ 
    # col no quebra-cabeça que ainda não foi preenchido --> rep com -1
    # return row, col tuple (ou (None, None) se não houver nenhum)
    # tenha em mente que estamos usando 0-8 para nossos índices
    for l in range(9):
        for c in range(9): # range(9) é 0, 1, 2, ... 8
            if puzzle[l][c] == -1:
                return l, c

    return None, None  #se nenhum espaço no quebra-cabeça estiver vazio (-1)

def valido(puzzle, guess, row, col):
    # descobre se o palpite na linha /
    # coluna do quebra-cabeça é um palpite válido
    # retorna True ou False

    # para um palpite ser válido /
    # então precisamos seguir as regras do sudoku
    # esse número não deve ser repetido na linha /
    # coluna ou quadrado 3x3 em que aparece

    # vamos começar com a linha
    valor_linha = puzzle[row]
    if guess in valor_linha:
        return False # se repetimos, então nosso palpite não é válido!
    # agora a coluna
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    coluna_valor = [puzzle[i][col] for i in range(9)]
    if guess in coluna_valor:
        return False

    # e então o quadrado
    inicio_linha = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    fim_linha = (col // 3) * 3

    for r in range(inicio_linha, inicio_linha + 3):
        for c in range(fim_linha, fim_linha + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def resolve_sudoku(puzzle):
    # resolva sudoku usando backtracking!
    # nosso quebra-cabeça é uma lista de listas /
    # onde cada lista interna é uma linha em nosso quebra-cabeça sudoku
    # retornar se existe uma solução
    # transforma o quebra-cabeça para ser a solução (se a solução existir)
    
    # passo 1: escolha algum lugar no quebra-cabeça para adivinhar
    row, col = encontre_proximo_vazio(puzzle)

    # se não sobrar nenhum lugar / 
    # então terminamos porque só permitimos entradas válidas
    if row is None:  # isso é verdade se nossa função encontre_proximo_vazio retornar None, None
        return True 
    
    # passo 2: se houver um lugar para colocar um número /
    # tente adivinhar entre 1 e 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # 38 / 5.000
        # passo 3: verifique se este é um palpite válido
        if valido(puzzle, guess, row, col):
            # passo 3.1: se este é um palpite válido /
            # coloque-o naquele ponto do quebra-cabeça
            puzzle[row][col] = guess
            # passo 4: então chamamos recursivamente nosso resolver!
            if resolve_sudoku(puzzle):
                return True
        
        # passo 5: não é válido ou se nada for retornado verdadeiro / 
        # então precisamos voltar atrás e tentar um novo número
        puzzle[row][col] = -1

    # passo 6: se nenhum dos números que tentamos funcionar /
    # então este quebra-cabeça é INSOLVÍVEL!!
    return False

if __name__ == '__main__':
    exemplo_quadro = [
        [4, -1, -1,    5, -1, 3,     -1, -1, -1],
        [9, 2, -1,   -1, 1, -1,     -1, 2, -1],
        [1, -1, -1,   -1, -1, 8,       -1, 4, 3],

        [-1, 6, -1,    -1, -1, 4,         -1, 5, 8],
        [-1, -1, 1,     -1, 7, -1,       -1, -1, -1],
        [-1, -1, -1,      -1, -1, -1,    9, -1, -1],

        [7, -1, -1,    -1, 4, -1,     -1, 3, 9],
        [-1, -1, -1,   -1, -1, 9,    6, -1, -1],
        [-1, 3, -1,   -1, -1, -1,    2, -1, -1]
    ]
    print(resolve_sudoku(exemplo_quadro))
    pprint(exemplo_quadro)