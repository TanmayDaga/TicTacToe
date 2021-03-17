import numpy as np
import random
from time import sleep


# create empty board
def create_board():
    return (np.array([[0, 0, 0]
                      [0, 0, 0]
                      [0, 0, 0]]))

# check for empty possibilities in board
def possibilities(board:np.array)
    l = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                l.append((i,j))

    return l

#TODO
# checks whether player has three of their marks in a horizontal row
