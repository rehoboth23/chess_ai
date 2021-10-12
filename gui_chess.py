from PyQt5 import QtGui, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget
import sys
import chess, chess.svg

from AlphaBetaAI import AlphaBetaAI
from IterativeDeepeningAI import IterativeDeepeningAI
from RandomAI import RandomAI
from MinimaxAI import MinimaxAI
from ChessGame import ChessGame
from HumanPlayer import HumanPlayer

import random


class ChessGui:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.game = ChessGame(player1, player2)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()
        self.over = 0

    def start(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.make_move)
        self.timer.start(10)
        self.display_board()

    def display_board(self):
        svgboard = chess.svg.board(self.game.board)
        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)

    def make_move(self):
        if self.game.board.is_game_over() and not self.over:
            print(self.game.board.outcome(), f"in {self.game.moves(self.game.board.outcome().winner)} moves")
            self.over += 1
        elif not self.game.board.is_game_over():
            self.game.make_move()
            print("making move, white turn " + str(self.game.board.turn))
        self.display_board()


if __name__ == "__main__":
    player1 = AlphaBetaAI(1, chess.WHITE)
    player2 = IterativeDeepeningAI(2, chess.BLACK)
    gui = ChessGui(player1, player2)
    gui.start()
    sys.exit(gui.app.exec_())
