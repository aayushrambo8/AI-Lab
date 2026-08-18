print("""
Human vs AI Tic-Tac-Toe
------------------------
AI uses the Minimax algorithm (with Alpha-Beta pruning) to play optimally.
Human is 'X', AI is 'O'. Board positions are numbered 1-9 like a phone keypad:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
""")

import math

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(0, 9, 3):
        row = board[i:i + 3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 6:
            print("-----------")
    print()


def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == EMPTY]


def check_winner(board, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_combos)


def is_full(board):
    return EMPTY not in board


def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves(board):
            board[move] = AI
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def best_ai_move(board):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice


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
    board = [EMPTY] * 9
    print("Welcome to Tic-Tac-Toe! You are X, the AI is O.")
    print_board(board)

    current_player = HUMAN  # human goes first

    while True:
        if current_player == HUMAN:
            move = get_human_move(board)
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = best_ai_move(board)
            board[move] = AI
            print(f"AI chose position {move + 1}")

        print_board(board)

        if check_winner(board, current_player):
            if current_player == HUMAN:
                print("You win! 🎉")
            else:
                print("AI wins! Better luck next time.")
            break

        if is_full(board):
            print("It's a draw!")
            break

        current_player = AI if current_player == HUMAN else HUMAN


if __name__ == "__main__":
    play_game()