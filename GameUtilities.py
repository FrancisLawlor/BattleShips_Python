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
        print (end="  ") 
        print (chr(ord('A')+c), end=" ")
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

