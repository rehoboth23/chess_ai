from random import random
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

    def max(self, board, depth, min_seen=float("inf")):
        if self.cut_off_test(board, depth):
            return super().calculate_score(board), None
        moves = sorted(board.legal_moves, key=lambda x: random())
        cost = -float("inf")
        res_move = None
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            cost_of_move, _ = self.min(board, depth + 1, cost)
            board.pop()
            if cost_of_move > cost:
                cost = cost_of_move
                res_move = move
            if min_seen < cost:
                break
        return cost, res_move

    def min(self, board, depth, max_seen=-float("inf")):
        if self.cut_off_test(board, depth):
            return super().calculate_score(board), None
        cost = float("inf")
        res_move = None
        moves = sorted(board.legal_moves, key=lambda x: random())
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            cost_of_move, _ = self.max(board, depth + 1, cost)
            board.pop()
            if cost_of_move < cost:
                cost = cost_of_move
                res_move = move
            if max_seen > cost:
                break
        return cost, res_move

    def calculate_score(self, board):
        return super().calculate_score(board)
