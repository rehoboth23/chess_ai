# chess_ai
#####*Class*: CS76
#####*Term*: Fall
#####*Year*: 2021
#####*Assignment*: PA1
#####*Name*: Okorie Kenechukwu
#####*Git Link: [Git Link](https://github.com/rehoboth23/chess_ai.git)


###Implementation
*MinimaxAI
        call MinimaxAI(p1, p2)
        p1 is the depth at which the AI should consider
        p2 player. Using the python chess module player as White is given as a boolean value `True` and player as black 
        is given as boolean value `False`  
        **Object Methods**

        choose_move(self, board: chess.Board): this will ask the AI to choose a move to play

        minmax_decision(self, board): will use the minmax algorith to select an optimal move based on the board 
        situation given

        max(self, board, depth): will select a move for the maximizer player

        min(self, board, depth): will select a move for the minimizer player

        calculate_score(self, board): will calculate the score for a given state.

        cut_off_test(self, board, depth): will check if a state is terminal

        make_moves(board): converts the board state into a list of legal/pseudo legal moves
       
*AlphaBetaAI 
        call AlphaBetaAI(p1, p2)
        p1 is the depth at which the AI should consider
        p2 player. Using the python chess module player as White is given as a boolean value `True` and player as black 
        is given as boolean value `False`  
        **Object Methods**
        
        max(self, board, depth, beta): will select a move for the maximizer player. the beta is the minimum score 
        recorded by the parent caller (i.e minmax_decision method or minimizer player). it's default is +inf.

        min(self, board, depth, alpha): will select a move for the minimizer player. the alpha is the maximum score 
        recorded by the parent caller (i.e maximizer player). it's default is -inf.

*IterativeDeepeningAI 
        call IterativeDeepeningAI(p1, p2)
        self.best_move is the best move seen in any decision-making process
        **Object Methods**

        minmax_decision(self, board): will use the minmax algorith to select an optimal move based on the board 
        situation given. This overrides the inherited methods and uses the same logic but with sequentially increasing 
        depth. It doesn't increase the depth if a depper look doesn't give a better solution.


*Scoring Logic
        The pieces of the chess board are scored pawns as 10, knights and bishops as 30, rooks as 50 and queens as 90.
        The value of the score is the valuation of the players pieces on the board.
        The score is also reduced by the value of the opponents officials on the board. Encourages the player to make 
        smart trades.
        If the board is a checkmate: if the winner is th player the score is increased by 500 to encourage the player to 
        work towards this outcome. if the player is the looser the score is reduced by 510 to avoid this outcome. The 
        player places priority on avoiding a checkmate over checkmating.
        The player uses similar logic to work for and avoid checks. The value of a check is capped at 50 to avoid making
        unreasonable sacrifices for a check (50 is also the minimum score required on a board to checkmate a lone king)
        The player will work towards a stalemate if it lacks the required amount of pieces to checkmate the opponent
        The player will also work towards a draw in the same situation


*Test Tools:
        The AI's track the number of nodes they visit.
        run test_moves_chess to check if alpha beta and minimax make the same decisions in a same game situation
        
        


    