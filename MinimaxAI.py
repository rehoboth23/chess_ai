from random import random
from time import sleep
import chess


class MinimaxAI:
    def __init__(self, depth, player):
        self.depth = depth
        self.player = player
        self.scores = {"p": 1, "n": 3, "b": 3, "r": 5, "q": 9, "k": 0}
        self.nodes_visited = 0
        self.name = "minmax"

    def choose_move(self, board: chess.Board):
        my_board = chess.Board(board.fen())
        return self.minmax_decision(my_board)

    def minmax_decision(self, board):
        cost, move = self.max(board, 0)
        if move is None or not len(str(move)):
            print(f"{board.outcome()}")
            sleep(100)
        print(f"making move {self.player} -> {move}")
        print(f"{self.name} after visiting {self.nodes_visited} nodes")
        return move

    def max(self, board, depth):
        if self.cut_off_test(board, depth):
            return self.calculate_score(board), None
        moves = sorted(board.legal_moves, key=lambda x: random())
        cost = -float("inf")
        res_move = None
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            cost_of_move, _ = self.min(board, depth + 1)
            board.pop()
            if cost_of_move > cost:
                cost = cost_of_move
                res_move = move
        return cost, res_move

    def min(self, board, depth):
        if self.cut_off_test(board, depth):
            return self.calculate_score(board), None
        cost = float("inf")
        res_move = None
        moves = sorted(board.legal_moves, key=lambda x: random())
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            cost_of_move, _ = self.max(board, depth + 1)
            board.pop()
            if cost_of_move < cost:
                cost = cost_of_move
                res_move = move
        return cost, res_move

    def calculate_score(self, board):
        score = 0
        fen = board.fen()
        score += 25 if board.is_check() and board.turn != self.player else 0
        score += -25 if board.is_check() and board.turn == self.player else 0
        score += 50 if board.is_checkmate() and board.outcome().winner == self.player else 0
        score += -50 if board.is_checkmate() and board.outcome().winner != self.player else 0
        # score -= 5 if board.is_capture(move) else 0
        for c in fen:
            if c.isalpha():
                s = self.scores[c.lower()]
                score += s if (c.islower() and self.player == chess.BLACK) or \
                              (c.isupper() and self.player == chess.WHITE) else -s
            elif c == " ":
                break
        score += 3 if board.is_stalemate() and score <= 0 else 0
        score += 3 if board.can_claim_fifty_moves() and score <= 0 else 0
        score += 3 if board.has_insufficient_material(not self.player) and score <= 0 else 0
        return score

    def cut_off_test(self, board, depth):
        return board.is_game_over() or depth >= self.depth
