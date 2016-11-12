import random 

#First things first, we will need to make the actually board and 
#environment for the game.

#Setting up variables to describe the board.
#0 represents an open space in the board
#1 represents the user/player
#2 represents the random AI player.

OPEN = 0
PLAYER = 1
COMPUTER = 2


class Board():
    board = []
    board_row = 3
    board_column = 3
    currentTurn = None
    firstTurn = False
    
    #when we create a board, all we really need to be sure of is 
    #that the board is empty.
    def __init__(self):
        self.reset()
    
    #reset clears the board, makes sure no user nor computer piece is on board.
    #Everything needs to be "Open"
    #reset does not require any parameter
    #reset returns nothing.
    def reset(self):
        self.board = []
        for x in range(0,3):
            self.board.append([OPEN,OPEN,OPEN])
            
    #isOpen checks if a space in the tic-tac-toe board is open.
    #isOpen takes in a (row) and (column) as parameters.
    #isOpen returns True if the desired spot in the board is open and returns False if the desired spot is taken.
    def isOpen(self, row, col):
        if self.board[row][col] is OPEN:
            return True
        return False
        
    #isClosed checks if the entire board is empty or not
    #isClosed does not take anything in
    #isClosed returns True if the board is full, False if the board is open.
    def isClosed(self):
        #in this method we check every coordinate pair to see if any spot is open, if it is, then the board cannot be closed.
        for row in range(0, 3):
            for col in range(0, 3):   
                if self.board[row][col] is OPEN:
                    return False
        return True
    
        
    #placeMove places the current turn's mark on the board.
    #placeMove takes in a (row), (column), and (currentPlayer)
    #placeMove returns True if the move was successful and returns False if the move was not successful.
    def placeMove(self, row, col, currentPlayer):
        #check to see if the desired move is open
        if row < 0 or row > 2 or col < 0 or col > 2:
            print ("Please choose another spot")
            return False 
        if self.isOpen(row,col) == True:
            self.board[row][col] = currentPlayer
            self.nextTurn()
            return True
        print ("Please choose another spot")
        return False
    
    #getTurn returns the current players turn.
    #getTurn simply returns whose turn it is
    def getTurn(self):
        return self.currentTurn
        
    #setTurn is a mutator that changes whose turn it is
    #setTurn takes in the player whose turn it is.
    def setTurn(self, player):
        self.currentTurn = player
        
    def setFirstTurn(self, turn):
        if turn is PLAYER:
            print("Player First")
            self.firstTurn = True
        else:
            print("Computer First")
            self.firstTurn = False
    
    def getFirstTurn(self):
        return self.firstTurn
    
            
    #nextTurn simply changes the player of the game.
    #nextTurn does not take in anything

    def nextTurn(self):
        #if it's the player's turn, the computer is next
        #else, vice versa.
        if self.getTurn() is PLAYER:
            self.setTurn(COMPUTER)
        else:
            self.setTurn(PLAYER)
        return self.getTurn()
        
    #validMoves is a method that determines which spots in the board are open.
    #validMoves does not take in any parameter
    #validMoves returns a list of available row and column coordinates in the board.
    def validMoves(self):
        moves = []
        #to figure out all the valid moves, we will traverse through the entire board,
        #checking each coordinate it if it is open.
        for row in range(0, 3):
            for col in range(0, 3):
                if self.isOpen(row,col):
                    moves.append([row,col])
        return moves
        
    #doMove is a method that allows a computer to do a random move.    
    #doMove does not take in any parameter.
    #doMove returns a move (coordinate pair).
    def doMove(self):
        
        #get a list of valid moves.
        validMoves = self.validMoves()
            
        #create a random number from 0 - length of valid moves     
        randomNumber = random.randrange(0, len(validMoves))
        
        #return a random coordinate pair.
        return validMoves[randomNumber]
            
    #winCondition is a method that checks the state of the board to see whether or not anyone has won.
    #winCondition does not take in any parameters
    #winCondition returns either PLAYER. COMPUTER, or NO WINNER
    def winCondition(self):
        
        #in tic tac toe can really only have 8 different ways to win.
        
        #3 comes from a horizontal victory in row 0, 1, 2
        for row in range(0, self.board_row):
            if self.board[row][0] != OPEN and self.board[row][0] == self.board[row][1] == self.board[row][2]:
                return self.board[row][0]

        #3 comes from a vertical victory in row 0, 1, 2        
        for col in range(0, self.board_column):
            if self.board[0][col] != OPEN and self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return self.board[0][col]    
        
        #1 comes from a diagonal starting from the upper left to bottom right.
        if self.board[0][0] != OPEN and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        
        #1 comes from a diagonal starting from the upper left to bottom right.
        if self.board[0][2] != OPEN and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[2][0]

        if self.isClosed() == True:
            return "NO WINNER"
        else:
            return None
        
    
        
        
    