class Game:
    def __init__(self) -> None:
        self.board = [[-1 for _ in range(7)] for _ in range(6)]
        self.player_turn = 0

    def add_coin(self, col_no):
        if col_no > 6:
            return
        # check if top row is already full
        if self.board[-1][col_no] != -1:
            return

        row = 0
        while self.board[row][col_no] != -1:
            row += 1
            pass
        self.board[row][col_no] = self.player_turn
        self.player_turn = 1 - self.player_turn
        return row

    def show_board(self):
        for i in self.board[::-1]:
            print(i)

    def check_win(self):
        """check for win condition on the board"""
        for row in self.board[::-1]:
            pass
        return None
