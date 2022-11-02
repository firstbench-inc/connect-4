"""
Our program, who art in memory,
    called by thy name;
  thy operating system run;
thy function be done at runtime
  as it was on development.
Give us this day our daily output.
And forgive us our code duplication,
    as we forgive those who
  duplicate code against us.
And lead us not into frustration;
  but deliver us from GOTOs.
    For thine is algorithm,
the computation, and the solution,
    looping forever and ever.
          Return;
"""

from re import A


class Game:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(7)] for _ in range(6)]
    
    def add_coin(self, col_no, player_no):
        if col_no > 6:
            return
        # check if top row is already full
        if self.board[-1][col_no] != 0:
            return

        row = 0
        while self.board[row][col_no] != 0:
            row += 1
            pass
        self.board[row][col_no] = player_no
    
    def show_board(self):
        for i in self.board[::-1]:
            print(i)
        


