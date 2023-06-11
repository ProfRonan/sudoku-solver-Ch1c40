"""Main module to run the program."""
def solve(board):
    """
    Função auxiliar para resolver o Sudoku usando a técnica de backtracking.

    Parâmetros:
    - board: lista de listas representando o tabuleiro de Sudoku (9x9). Os espaços vazios são representados por 0.

    Retorna:
    - True se o tabuleiro for resolvido com sucesso, False caso contrário.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    board[row][col] = num

                    if is_valid(board) and solve(board):
                        return True

                    board[row][col] = 0

                return False

    return True


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """
    Resolve um tabuleiro de Sudoku incompleto.

    Parâmetros:
    - board: lista de listas representando o tabuleiro de Sudoku (9x9). Os espaços vazios são representados por 0.

    Retorna:
    - O tabuleiro completo de Sudoku.

    Lança:
    - ValueError: se o tabuleiro passado for impossível de resolver.
    """
    if not is_valid(board):
        raise ValueError("Tabuleiro inválido")

    if solve(board):
        return board
    else:
        raise ValueError("Sudoku impossível de resolver")


def is_valid(board: list[list[int]]) -> bool:
    """
    Verifica se um tabuleiro de Sudoku é válido.

    Parâmetros:
    - board: lista de listas representando o tabuleiro de Sudoku (9x9).

    Retorna:
    - True se o tabuleiro for válido, False caso contrário.
    """
    def is_valid_row(row):
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_column(col):
        seen = set()
        for row in board:
            num = row[col]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_valid_region(start_row, start_col):
        seen = set()
        for row in range(start_row, start_row + 3):
            for col in range(start_col, start_col + 3):
                num = board[row][col]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)
        return True

    for row in board:
        if not is_valid_row(row):
            return False

    for col in range(9):
        if not is_valid_column(col):
            return False

    for start_row in range(0, 9, 3):
        for start_col in range(0, 9, 3):
            if not is_valid_region(start_row, start_col):
                return False

    return True