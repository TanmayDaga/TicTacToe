"""
# signs -> 1,2
"""
import random


class TicTacToeBoard:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.possibility = []
        self.possibility_generator()

    def possibility_generator(self) -> None:
        for x in range(len(self.board)):
            for y in range(len(self.board)):
                if self.board[x][y] == 0:
                    self.possibility.append((x, y))

    def update_possibility(self) -> None:
        for index, items in enumerate(self.possibility):
            if self.board[items[0]][items[1]] != 0:
                self.possibility.pop(index)

    def change_sign(self, x, y, sign) -> bool:
        if self.board[x][y] == 0:
            self.board[x][y] = sign
            return True
        return False

    def row_win(self, sign) -> bool:
        for x in range(len(self.board)):
            win = True
            for y in range(len(self.board)):
                if self.board[x][y] != sign:
                    win = False

            if win:
                return win
        return False

    def column_win(self, sign) -> bool:
        for x in range(len(self.board)):
            win = True
            for y in range(len(self.board)):
                if self.board[y][x] != sign:
                    win = False
            if win:
                return win
        return False

    def diagonal_win(self, sign) -> bool:
        win = True
        for x in range(len(self.board)):
            if self.board[x][x] != sign:
                win = False
        if win:
            return win
        win = True
        for x, y in zip(reversed(range(len(self.board))), range(len(self.board))):
            if self.board[x][y] != sign:
                win = False
        if win:
            return win
        return False

    def random_play(self):
        while True:
            row_random = random.randrange(0, len(self.board))
            column_random = random.randrange(0, len(self.board))
            if self.change_sign(row_random, column_random, "2"):
                return row_random, column_random


if __name__ == '__main__':
    ex = TicTacToeBoard()
