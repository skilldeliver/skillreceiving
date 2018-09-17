def findindexes(squares, move):
    """ Return the matrix indexes of the move """

    for index, row in enumerate(squares): # iterate the rows
        for index2, el in enumerate(row): # iterate every element in the row
            if el == move:
                return (index, index2) # return the indexes of the move if it on the board

def white_black_move(board, squares, move, mode):
    """ Return the changed board and nochange boolean """

    if mode == "white":
        PIECE, OPOSITE, NUM, rank = ("P", "p", 1, 4)
    elif mode == "black":
        PIECE, OPOSITE, NUM, rank = ("p", "P", -1, 3)

    nochange = True
    if "x" in move: # is taking
        inxs = findindexes(squares, move[2:]) # find the indexes of the square which will be taken
        if inxs: # the square which is going to be taken is found on the board
            if board[inxs[0]][inxs[1]] is OPOSITE: # on the square which is taken there is a oposite piece
                inxs2 = findindexes(squares, f"{move[0]}{abs(inxs[0] - 8) - NUM}") # find the indexes of the current piece
                if board[inxs2[0]][inxs2[1]] is PIECE: # check if it is a current piece
                    board[inxs2[0]][inxs2[1]] = "." # replace the prev current piece square with dot
                    board[inxs[0]][inxs[1]] = PIECE # replace the oposite piece with current spiece
                    nochange = False # change the boolean because there is a change
    else: # is moving
        inxs = findindexes(squares, move) # find the indexes of the move in the board matrix
        if inxs: # the square is found on the board
            if not(board[inxs[0]][inxs[1]] is OPOSITE): # the square is not taken by oposite piece
                if board[inxs[0] + NUM][inxs[1]] is PIECE:              
                    # the move is only one square forward or if it is on the forth/third row it can be two squares forward
                    board[inxs[0] + NUM][inxs[1]] = "." # replace the prev current piece square with dot
                    board[inxs[0]][inxs[1]] = PIECE # replace the new square with current piece
                    nochange = False # change the boolean because there is a change
                elif inxs[0] is rank and board[inxs[0] + (NUM * 2)][inxs[1]] is PIECE:
                    board[inxs[0] + NUM * 2][inxs[1]] = "." # replace the prev current piece square with dot
                    board[inxs[0]][inxs[1]] = PIECE # replace the new square with current piece
                    nochange = False # change the boolean because there is a change

    return board, nochange


def pawn_move_tracker(moves):
    board = [
    [".",".",".",".",".",".",".","."],
    ["p","p","p","p","p","p","p","p"],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".","."],
    ["P","P","P","P","P","P","P","P"],
    [".",".",".",".",".",".",".","."]
    ]

    squares = [
    ["a8","b8","c8","d8","e8","f8","g8","h8"],
    ["a7","b7","c7","d7","e7","f7","g7","h7"],
    ["a6","b6","c6","d6","e6","f6","g6","h6"],
    ["a5","b5","c5","d5","e5","f5","g5","h5"],
    ["a4","b4","c4","d4","e4","f4","g4","h4"],
    ["a3","b3","c3","d3","e3","f3","g3","h3"],
    ["a2","b2","c2","d2","e2","f2","g2","h2"],
    ["a1","b1","c1","d1","e1","f1","g1","h1"]
    ]

    for index, move in enumerate(moves):

        if not index % 2: # white on move
            board, nochange = white_black_move(board, squares, move, "white")
        else: # black move
            board, nochange = white_black_move(board, squares, move, "black")

        if nochange: # if there is no change therfore the move is invalid
            return f"{move} is invalid"

    return board