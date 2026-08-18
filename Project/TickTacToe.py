import math

HUMAN, AI, EMPTY = "X", "O", " "
WIN_COMBOS = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)              # Diagonals
)


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")
    print()


def check_winner(board, player):
    return any(all(board[i] == player for i in combo) for combo in WIN_COMBOS)


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def minimax(board, depth, is_ai, alpha=-math.inf, beta=math.inf):
    if check_winner(board, AI):
        return 10 - depth, None
    if check_winner(board, HUMAN):
        return depth - 10, None
    moves = available_moves(board)
    if not moves:
        return 0, None

    player = AI if is_ai else HUMAN
    best_score = -math.inf if is_ai else math.inf
    best_move = moves[0]

    for move in moves:
        board[move] = player
        score, _ = minimax(board, depth + 1, not is_ai, alpha, beta)
        board[move] = EMPTY

        if is_ai and score > best_score:
            best_score, best_move = score, move
            alpha = max(alpha, best_score)
        elif not is_ai and score < best_score:
            best_score, best_move = score, move
            beta = min(beta, best_score)

        if beta <= alpha:
            break

    return best_score, best_move


def get_human_move(board):
    while True:
        try:
            choice = int(input("Your move (1-9): ")) - 1
            if choice in available_moves(board):
                return choice
            print("That spot is taken or invalid. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")


def play_game():
    print("""
Human vs AI Tic-Tac-Toe
------------------------
AI uses Minimax (with Alpha-Beta pruning) to play optimally.
Human is 'X', AI is 'O'. Board positions are numbered 1-9 like a phone keypad:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
""")
    board = [EMPTY] * 9
    print_board(board)
    current_player = HUMAN

    while True:
        if current_player == HUMAN:
            move = get_human_move(board)
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            _, move = minimax(board, 0, True)
            board[move] = AI
            print(f"AI chose position {move + 1}")

        print_board(board)

        if check_winner(board, current_player):
            print("You win! 🎉" if current_player == HUMAN else "AI wins! Better luck next time.")
            break
        if EMPTY not in board:
            print("It's a draw!")
            break

        current_player = AI if current_player == HUMAN else HUMAN


if __name__ == "__main__":
    play_game()