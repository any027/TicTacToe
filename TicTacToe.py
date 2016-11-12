import random
from board import Board, OPEN, PLAYER, COMPUTER

def displayMark(coord):
    if coord == PLAYER:
        return 'O'
    elif coord == COMPUTER:
        return 'X'
    else:
        return ' '

#displayBoard prints out the current state of the board
def displayBoard(board):
    print (" 0          1         2      ")
    for x in range(0, board.board_row):
        print ("-----------------------------")
        print ("|    %s    |   %s     |    %s   |"
        % \
(displayMark(board.board[x][0]), displayMark(board.board[x][1]), displayMark(board.board[x][2])))
    print ("-----------------------------")
    
print ("Welcome to Anthony's Tic-Tac-Toe!")
choice = None
board = Board()
displayBoard(board)
board.setTurn(PLAYER)

#have an infinite while loop while the game state has not ended.
while board.winCondition() == None:
    if board.getTurn() is PLAYER:
        row = int(input("Please choose a row coordinate from 0 to 2 "))
        col = int(input("Now please choose a column coordinate from 0 to 2 "))
    else:
        print ("Waiting for computer to make a move")
        move = board.doMove()
        row = move[0]
        col = move[1]
    
    board.placeMove(row,col,board.getTurn())
    displayBoard(board)
            
if board.winCondition() == PLAYER:
    print ('Congratulations!')
elif board.winCondition() == COMPUTER:
    print ('Maybe next time!')
else:
    print ("No Winner")