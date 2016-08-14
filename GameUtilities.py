import os

def clear_screen():
	os.system('clear')

# Prints out the board, taking each of the two lists as arguments.
# Involves printing two lists side by side, the current player, and the disguised board.
def print_board(player1, player2):
    print (" ", end=" ")

    # Print out the letters on the board.
    c=0
    for i in range (0, 16):
        print (end = "  ") 
        print (chr(ord('A') + c), end = " ")
        c=c+1

    print ()

    # Print the numbers on the board.
    c=0
    d=0
    num = 1
    for i in range (0, 16):
        if(num<10):
            print (end=" ")
            print (chr(ord('1')+c), end=" ")
            c=c+1
            if(num<11):
                num=num+1
        if(num>10):
            print ('1', end="")
            print (chr(ord('0')+d), end=" ")
            d=d+1
            num=num+1

        if(num==10):
            num=num+1

        # Print a line from player1's list.
        for j in range (0,8):
            print (player1[i][j], end="  ")

        # Print a line from player2's list.
        for k in range (0,8):
            print (player2[i][k], end="  ")

        # New line.
        print ()

def hit_board(x, y, board):

    # If the x co-ordinate is greater than 7 i.e. it is on the right hand side of the board it needs to be reduced as each side is an individual 2D list.
    if (x > 7):
        x = x - 8

    if ((board[y][x] != " _") & (board[y][x] != " X")):
            print ("You got a hit!")

    board[y][x]=' X'

def check_win(player,coordinates_x, coordinates_y):
    win = True
    for i in range (0, len(coordinates_x)):
        if player[coordinates_x[i]][coordinates_y[i]]!=" X":
            print (coordinates_x[i])
            print (coordinates_y[i])
            win=False

    return win

