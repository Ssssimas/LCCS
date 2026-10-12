board = []
for i in range(9):
    board.append("□")

def printboard():
    print (board[0], board[1], board[2], sep= " ")
    print (board[3], board[4], board[5], sep= " ")
    print (board[6], board[7], board[8], sep= " ")

def setboard(pos, character):
    if character == "X" or character == "O" and board[pos] == "□":
        board[pos] = character
        printboard()
        PlayerInput()
    else:
        print("Invalid Move")
        PlayerInput()

def PlayerInput():
    PlayerMove = input("Select a number 1-9")
    PlayerMove = int(PlayerMove)- 1
    setboard(PlayerMove, "X")
    
PlayerInput()
    
    
    