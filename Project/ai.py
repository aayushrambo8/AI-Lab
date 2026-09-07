"""
ai.py
-----
Minimax search algorithm with Alpha-Beta Pruning for Tic-Tac-Toe AI.
"""

import math
from game import EMPTY, checkWinner, availableMoves


def minimax(board, depth, isMaximizing, aiSymbol, humanSymbol,
            alpha=-math.inf, beta=math.inf):
    """Recursive alpha-beta search algorithm to determine the optimal move score."""
    if checkWinner(board, aiSymbol):
        return 10 - depth, None
    if checkWinner(board, humanSymbol):
        return depth - 10, None

    moves = availableMoves(board)
    if not moves:
        return 0, None

    player = aiSymbol if isMaximizing else humanSymbol
    bestScore = -math.inf if isMaximizing else math.inf
    bestMove = moves[0]

    for move in moves:
        board[move] = player
        score, _ = minimax(board, depth + 1, not isMaximizing,
                            aiSymbol, humanSymbol, alpha, beta)
        board[move] = EMPTY

        if isMaximizing and score > bestScore:
            bestScore, bestMove = score, move
            alpha = max(alpha, bestScore)
        elif not isMaximizing and score < bestScore:
            bestScore, bestMove = score, move
            beta = min(beta, bestScore)

        if beta <= alpha:
            break  # Prune branch

    return bestScore, bestMove


def getAiMove(board, aiSymbol, humanSymbol):
    """Calculates and returns the best move for the AI using Minimax with Alpha-Beta pruning."""
    _, move = minimax(board, 0, True, aiSymbol, humanSymbol)
    return move
