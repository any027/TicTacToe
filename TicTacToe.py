import random
import time
from board import Board, OPEN, PLAYER, COMPUTER

def displayMark(coord):
    if board.getFirstTurn():
        if coord == PLAYER:
            return 'X'
        elif coord == COMPUTER:
            return 'O'
        else:
            return ' '
    else:
        if coord == PLAYER:
            return 'O'
        elif coord == COMPUTER:
            return 'X'
        else:
            return ' '

#displayBoard prints out the current state of the board
def displayBoard(board):
    print ("     0          1         2      ")
    for x in range(0, board.board_row):
        print ("  -----------------------------")
        print (str(x) + " |    %s    |   %s     |    %s   |" 
        % \
(displayMark(board.board[x][0]), displayMark(board.board[x][1]), displayMark(board.board[x][2])))
    print ("  -----------------------------")
    
print ("Welcome to Anthony's Tic-Tac-Toe!")

print("Please choose who will go first!")
print("Please press (F)irst or 1 to go first")
print("or please press (S)econd or 2 to go second")
choice = None

while not choice in ["F","f","1","S","s","2","Q","q"]:
    if choice == None:
        choice = input("Please put in an input\n" )
    else:
        choice = input("Please put in a proper input\n" )
        
if choice == "q" or choice == "Q":
    print ("Thank you for playing!")
    exit()
elif choice == "F" or choice == 'f' or choice == "1":
    choice = None
    board = Board()
    displayBoard(board)
    board.setFirstTurn(PLAYER)
    board.setTurn(PLAYER)
else:
    choice = None
    board = Board()
    displayBoard(board)
    board.setFirstTurn(COMPUTER)
    board.setTurn(COMPUTER)
    move = board.doMove()
    row = move[0]
    col = move[1]

#have an infinite while loop while the game state has not ended.
while board.winCondition() == None:
    if board.getTurn() is PLAYER:
        row = int(input("Please choose a row coordinate from 0 to 2 "))
        col = int(input("Now please choose a column coordinate from 0 to 2 "))
    else:
        print ("Waiting for computer to make a move")
        time.sleep(2)
        move = board.doMove()
        row = move[0]
        col = move[1]
    
    board.placeMove(row,col,board.getTurn())
    displayBoard(board)
            
if board.winCondition() == PLAYER:
    print ('Congratulations! You Won!')
elif board.winCondition() == COMPUTER:
    print ('Sorry, you lost! Maybe next time!')
else:
    print ("No Winner")