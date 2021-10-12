from copy import copy

import chess

from AlphaBetaAI import AlphaBetaAI


class IterativeDeepeningAI(AlphaBetaAI):
    def __init__(self, depth, player):
        super().__init__(depth, player)
        self.name = "iterative_deepening"
        self.best_move = (-float("inf"), None)

    def choose_move(self, board: chess.Board):
        my_board = chess.Board(board.fen())
        return self.minmax_decision(my_board)

    def minmax_decision(self, board):
        self.nodes_visited = 0
        true_depth = self.depth
        for i in range(1, true_depth + 1):
            self.depth = i
            score, move = self.max(board, 0)
            if score >= self.best_move[0]:
                self.best_move = (score, move)
            else:
                break
        score, move = self.best_move
        print(f"{self.name} making move {self.player} -> {move} after visiting {self.nodes_visited} nodes")
        if self.player:
            open(self.name, "a").write(f"{str(move)}: {score}")
        self.best_move = (-float("inf"), None)
        self.depth = true_depth
        return move

    def max(self, board, depth, beta=float("inf")):
        return super().max(board, depth, beta)

    def min(self, board, depth, alpha=-float("inf")):
        return super().min(board, depth, alpha)

    def calculate_score(self, board):
        return super().calculate_score(board)
