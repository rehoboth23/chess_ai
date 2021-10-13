from time import sleep

import chess


class MinimaxAI:
    def __init__(self, depth, player):
        self.depth = depth
        self.player = player
        self.scores = {"p": 10, "n": 30, "b": 30, "r": 50, "q": 90, "k": 0}
        self.nodes_visited = 0
        self.name = "minmax"

    def choose_move(self, board: chess.Board):
        if self.nodes_visited == 0:
            f1 = open(self.name, "r+")
            f1.truncate(0)
            f1.close()
        my_board = chess.Board(board.fen())
        return self.minmax_decision(my_board)

    def minmax_decision(self, board):
        # self.nodes_visited = 0
        score, move = self.max(board, 0)
        print(f"{self.name} {'white' if self.player else 'black'} making move {self.player} -> {move} after visiting {self.nodes_visited} nodes")
        if self.player:
            open(self.name, "a").write(f"{str(move)}: {score}\n")
        return move

    def max(self, board, depth):
        # chooses the best move for the maximizer player by maximizing the score.
        if self.cut_off_test(board, depth):
            return self.calculate_score(board), None
        moves = self.make_moves(board)
        score = -float("inf")  # if the player doesn't make a move interpret it as the lowest possible score
        res_move = None
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            score_of_move, _ = self.min(board, depth + 1)
            board.pop()
            if score_of_move >= score:
                score = score_of_move
                res_move = move
        return score, res_move

    def min(self, board, depth):
        # chooses best move for the minimizer player by minimizing the score which reflects the best choice for the
        # maximizer player
        if self.cut_off_test(board, depth):
            return self.calculate_score(board), None
        score = float("inf") # if the player doesn't make a move interpret it as the highest possible score
        res_move = None
        moves = self.make_moves(board)
        for move in moves:
            self.nodes_visited += 1
            board.push(move)
            score_of_move, _ = self.max(board, depth + 1)
            board.pop()
            if score_of_move <= score:
                score = score_of_move
                res_move = move
        return score, res_move

    def calculate_score(self, board):
        # a higher score reflects a better outcome for the maximizer player and a lower score a worse outcome
        score = 0
        other_score = 0
        fen = board.fen()
        for c in fen:  # score depends on the number and value of players pieces on the board
            if c.isalpha():
                s = self.scores[c.lower()]
                if (c.islower() and not self.player) or \
                        (c.isupper() and self.player):
                    score += s
                elif c.lower() in {"q", "n", "b", "r"}:
                    other_score += s
            elif c == " ":
                break

        # can allow the player to make sacrifices to win by prioritizes taking opponents officials
        score -= other_score
        # work towards a check and avoid being checked but not at the expense of any players
        score += 50 if board.is_check() and board.turn != self.player else 0
        score -= 50 if board.is_check() and board.turn == self.player else -1
        # work towards a check mate and prioritise over any other score.
        # avoiding being checkmated is more important than checkmating
        score += 500 if board.is_checkmate() and board.outcome().winner == self.player else 0
        score -= 510 if board.is_checkmate() and board.outcome().winner != self.player else 0
        # work to wards a stalemate when score < 5 i.e has insufficient material to carry out a checkmate
        # on a lone king. avoid stalemates if you can checkmate
        score += 30 if board.is_stalemate() and score < 50 else 0
        # work towards a draw when score < 5 i.e has insufficient material to carry out a checkmate
        # on a lone king. avoid draws if you can checkmate
        score += 30 if board.can_claim_fifty_moves() and score < 50 else 0
        return score

    def cut_off_test(self, board, depth):
        # check if the search is at a terminal tate
        return board.is_game_over() or depth > self.depth

    @staticmethod
    def make_moves(board):
        # get set of legal moves from board and convert to a list
        return list(board.legal_moves)
