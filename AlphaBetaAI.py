from time import sleep

import chess

from MinimaxAI import MinimaxAI


class AlphaBetaAI(MinimaxAI):
    def __init__(self, depth, player):
        super().__init__(depth, player)
        self.name = "alpha_beta"

    def choose_move(self, board: chess.Board):
        return super().choose_move(board)

    def minmax_decision(self, board):
        return super().minmax_decision(board)

    def max(self, board, depth, beta=float("inf")):
        if self.cut_off_test(board, depth):
            return super().calculate_score(board), None
        moves = self.make_moves(board)
        score = -float("inf")
        res_move = None
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            score_of_move, _ = self.min(board, depth + 1, score)
            board.pop()
            if score_of_move >= score:
                score = score_of_move
                res_move = move
            if beta < score:
                break
        return score, res_move

    def min(self, board, depth, alpha=-float("inf")):
        if self.cut_off_test(board, depth):
            return super().calculate_score(board), None
        score = float("inf")
        res_move = None
        moves = self.make_moves(board)
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            score_of_move, _ = self.max(board, depth + 1, score)
            board.pop()
            if score_of_move <= score:
                score = score_of_move
                res_move = move
            if alpha > score:
                break
        return score, res_move

    def calculate_score(self, board):
        return super().calculate_score(board)
