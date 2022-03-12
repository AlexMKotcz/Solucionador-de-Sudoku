def encontrar_proxima_posicao_vazia(puzzle):
    """Itera pelo puzzle até encontrar uma posição vazia, retornando ela caso exista.
    """
    
    #Itera por cada linha e coluna do puzzle até encontrar o valor -1 (posição vazia)
    for l in range(9):
        for c in range(9):
            if puzzle[l][c] == -1:
                return l, c
    
    #Se não encontra o valor, todas as células estão preenchidas e não existe uma posição vazia
    return None, None


def chute_valido(puzzle, chute, linha_chute, coluna_chute):
    """Verifica se um chute é valido para uma posição do puzzle, retornando True ou False.
    """

    #Cria uma lista de valores da linha para a coluna do chute.
    valores_da_linha = puzzle[linha_chute]
    #Verifica se o chute já existe nos valores da linha.
    if chute in valores_da_linha:
        return False #Se existir, retorna que o chute não é válido.

    #Cria uma lista de valores da coluna para a linha do chute.
    valores_da_coluna = [puzzle[i][coluna_chute] for i in range(9)]
    #Verifica se o chute já existe nos valores da coluna.
    if chute in valores_da_coluna:
        return False #Se existir, retorna que o chute não é válido.

    #Pega a posição de início da linha e da coluna (divisão por quadrantes do Sudoku)
    inicio_linha = (linha_chute // 3) * 3
    inicio_coluna = (coluna_chute // 3) * 3

    #Itera pelos demais valores do quadrante do chute, verificando se o chute já existe naquele quadrante.
    for linha in range (inicio_linha, inicio_linha + 3):
        if linha != linha_chute: #A linha_chute já foi validada anteriormente, então ela é ignorada para ganhos de performance.
            for coluna in range (inicio_coluna, inicio_coluna + 3):
                if coluna != coluna_chute: #A coluna_chute já foi validada anteriormente, então ela é ignorada para ganhos de performance.
                    if puzzle[linha][coluna] == chute:
                        return False #Se existir o valor do chute no quadrante, retorna que o chute não é válido.

    #Se o valor do chute não existe na linha, coluna ou quadrante do chute, então ele é válido.
    return True


def solucionar_sudoku(puzzle):
    """Soluciona um puzzle de sudoku recursivamente;
    O puzzle é uma lista de listas, onde cada lista de dentro é uma linha no nosso puzzle de sudoku;
    Retorna se a solução existe;
    Altera o puzzle para ele ser a solução (caso exista).
    """
    
    #O primeiro passo é verificar se esse puzzle possui um valor vazio, e armazenar a posição desse valor
    linha, coluna = encontrar_proxima_posicao_vazia(puzzle)
    if linha is None:
        return True #Se não existir um valor vazio, o Puzzle está completo

    #Se existe uma posição vazia, chute um número entre 1 e 9
    for valor_chutado in range(1, 10): #1, 2, 3, ..., 8, 9
        #Verifica se esse chute é válido
        if chute_valido (puzzle, valor_chutado, linha, coluna):
            #Se for válido, então substitua o valor do puzzle pelo chute
            puzzle[linha][coluna] = valor_chutado

            #Chamamos o método recursivamente
            if solucionar_sudoku(puzzle):
                return True
        
        #Se o chute não é válido ou se nada retornar True, voltamos atras e tentamos um novo chute
        puzzle[linha][coluna] = -1
    
    #Se nenhum número tentado funcionar, então o puzzle não tem solução
    return False

if __name__ == '__main__':
    jogo_sudoku = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solucionar_sudoku(jogo_sudoku))
    print(jogo_sudoku)