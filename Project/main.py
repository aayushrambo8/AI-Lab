"""
main.py
-------
Pure Python CLI interface for Tic-Tac-Toe Minimax AI.
"""

from game import EMPTY, checkWinner, availableMoves
from ai import getAiMove


def printBoard(board):
    print("\n")
    for row in range(3):
        spots = [board[row * 3 + col] if board[row * 3 + col] != EMPTY else str(row * 3 + col + 1) for col in range(3)]
        print(f" {spots[0]} | {spots[1]} | {spots[2]} ")
        if row < 2:
            print("-----------")
    print("\n")


def playGame():
    board = [EMPTY] * 9
    print("==========================================")
    print("  Tic-Tac-Toe — Pure Python Minimax AI")
    print("==========================================")

    symbolChoice = input("Play as (X/O) [default X]: ").strip().upper()
    humanSymbol = "O" if symbolChoice == "O" else "X"
    aiSymbol = "O" if humanSymbol == "X" else "X"

    firstChoice = input("Who goes first? (1: You, 2: AI) [default 1]: ").strip()
    humanTurn = firstChoice != "2"

    while True:
        printBoard(board)

        if checkWinner(board, humanSymbol):
            print("🎉 Congratulations! You won!")
            break
        if checkWinner(board, aiSymbol):
            print("🤖 AI wins! (Minimax optimal play)")
            break
        if not availableMoves(board):
            print("🤝 It's a draw!")
            break

        if humanTurn:
            moves = availableMoves(board)
            try:
                moveStr = input(f"Your move ({humanSymbol}) [1-9]: ").strip()
                move = int(moveStr) - 1
                if move not in moves:
                    print("Invalid move! Try again.")
                    continue
                board[move] = humanSymbol
                humanTurn = False
            except ValueError:
                print("Please enter a valid number (1-9).")
                continue
        else:
            print("AI is computing move...")
            aiMove = getAiMove(board, aiSymbol, humanSymbol)
            board[aiMove] = aiSymbol
            print(f"AI chose position {aiMove + 1}")
            humanTurn = True


if __name__ == "__main__":
    playGame()
