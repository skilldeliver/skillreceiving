# Tic-Tac-Toe

import random

def drawBoard(board):
    # This function prints out the board that was passed.

    # "board" is  a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[3] + '|' + board[2] + '|' + board[1])


list = [" ", " ", " ", " ", "X", "O", " ", "X", " ", "O"]

print(drawBoard(list))









