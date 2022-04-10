import random
from turtle import position
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]
currentPlayer = "X"
winner = None
gameRunning = True


#Printing the game board
def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])
    print("------")
printBoard(board)
 
#Taking the player input
def playerInput(board): 
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] == "_":
        board[inp-1] = currentPlayer
    else:
        print("Oops! The space already occupied by another player!")
    
#Checking for the win or tie
def checkHorizontile(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board [5] and board [3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkRow(board): 
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board [7] and board [1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board [6] and board [2] != "_":
        winner = board[2]
        return True
   
def checkTie(board):
    if "_" not in board:
        printBoard(board)
        print(" It is a tie!")
        gameRunning = False
 
def checkWin():
    if checkDiag(board) or checkHorizontile(board) or checkRow(board):
        print(f"The winner is {winner}")
        
#Switching the player 
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#Computer 
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switchPlayer()
#check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)