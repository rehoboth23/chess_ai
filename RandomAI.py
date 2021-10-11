import random
from time import sleep


class RandomAI():
    def __init__(self):
        pass

    def choose_move(self, board):
        moves = list(board.legal_moves)
        if not len(moves):
            print(f"{board.outcome()}")
            sleep(100)
        move = random.choice(moves)
        print("Random AI recommending move " + str(move))
        return move
