EMPTY = " "
winCombos = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # Columns
    (0, 4, 8), (2, 4, 6),              # Diagonals
)


def checkWinner(board, player):
    return any(all(board[i] == player for i in combo) for combo in winCombos)


def availableMoves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]
