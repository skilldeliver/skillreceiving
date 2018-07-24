#https://en.wikipedia.org/wiki/Tic-tac-toe

#1.Win: If the player has two in a row, they can place a third to get three in a row.

#2.Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.

#3.Fork: Create an opportunity where the player has two threats to win 

#4.Blocking an opponent's fork:  If there is only one possible fork for the opponent, the player should block it

#5.Center: A player marks the center. 

#6.Opposite corner: If the opponent is in the corner, the player plays the opposite corner.

#7.Empty corner: The player plays in a corner square.

#8.Empty side: The player plays in a middle square on any of the 4 sides.

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def checkForWin(b, l):
    if ((b[0] == l and b[1] == l and b[2] == l) or
    (b[3] == l and b[4] == l and b[5] == l) or
    (b[6] == l and b[7] == l and b[8] == l) or
    (b[0] == l and b[3] == l and b[6] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[0] == l and b[4] == l and b[8] == l) or
    (b[6] == l and b[4] == l and b[2] == l)): return 1

    return 0

def copyBoard(b):
    secBoard = []
    for i in b:
        secBoard.append(i)
    return secBoard

def freePlaces(b):
    freeplaces = []
    for i in b:
        if i != "x" and i != "o":
            freeplaces.append(i)

    return freeplaces

def WinBlock(b, l):
    freeplace = freePlaces(b)
    for i in range(9):
        useCopy = copyBoard(b)
        if i in freeplace:
            useCopy[i] = l
            if checkForWin(useCopy, l):
                return i

def Fork(b, l):



print(Fork(board, "x"))

#def AImove(b, cL, pL):
#    if WinBlock(b, cL) != None: return WinBlock(b, cL)
#    elif WinBlock(b, pL) != None: return WinBlock(b, pL)


#board[blockInd] = cL
#print(board)

#firstTurn = input().lower()
#if firstTurn == "x": pL = "x"; cL = "o"
#else: pL = "o"; cL = "x"

#game = True
#while game:
#    if checkForWin(board, cL): print("AI wins"); game = False
#    elif checkForWin(board, cL): print("Player wins"); game = False
#    elif freePlaces(board): print("Tie"); game = False



