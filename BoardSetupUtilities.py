import random

def set_up_board(player):
    for i in range (0, 16):
        player.append([]) # Create an empty list in every element of the player list.

    for i in range (0, 16):
        for j in range (0,8):
            player[i].append(" _") # Go through every element and assign " _"

# This function returns either the number 0 or 1. Which ever number is returned will be used to randomly choose if the ships are horizontal or vertical.
def vertical_or_horizontal():
    value = random.randint(0, 1)
    if value==0:
        return 0
    if value==1:
        return 1

def place_ship(board, letter):

    # Randomise coordinate co-ordinate for "center" of ship. Remaining ship co-ordinates will be selected in relation to it.
    x=random.randint(0,7)
    y=random.randint(0,15)

    # Randomise whether ship is horizontal or vertical
    position=vertical_or_horizontal() # Vertical = 0, Horizontal = 1

    # Check if ship to be placed clashes with any existing ship's co-ordinates.
    if (doesnt_clash(board, x, y, position, letter)): 
        print ("works, lad", end = "")
        if((position==0)):

            # If center of ship is at top row or bottom row of board, move it so it can fit.
            if(y==0):
                y=1
            if(y==15):
                y=14

            board[y][x]= " " + letter

            if((letter != 'F')):
                board[y-1][x]= " " + letter
            if((letter != 'F') & (letter != 'D')):
                board[y+1][x]= " " + letter
            if((letter != 'F') & (letter != 'D') & (letter!= 'C')):
                if(y==14):
                    board[y-2][x]= " " + letter
                if(y<14):
                    board[y+2][x]= " " + letter

        if(position==1):

            # If center of ship is at top column or bottom column of board move it so it can fit.
            if (x==0):
                x=1
            if (x==7):
                x=6

            board[y][x]= " " + letter

            if(letter != 'F'):
                board[y][x-1]= " " + letter
            if((letter != 'F') & (letter != 'D')):
                board[y][x+1]= " " + letter
            if((letter != 'F') & (letter != 'D') & (letter!= 'C')):
                if (x>1):
                    board[y][x-2]= " " + letter
                if (x==1):
                    board[y][x+2]= " " + letter
    else:
        place_ship(board, letter)
        print ("doesn't work", end = "")

def doesnt_clash(board, x, y, orientation, letter):

    if (orientation == 0):
        if (y == 0):
            y = 1
        if (y == 15):
            y = 14

    if (orientation == 1):
        if (x == 0):
            x = 1
        if (x == 7):
            x = 6

    if (board[y][x] != " _"):
        return False

    if (orientation == 0):
        if ((letter != 'F')):
            if (board[y-1][x] != " _"):
                return False
        if ((letter != 'F') & (letter != 'D')):
            if (board[y+1][x] != " _"):
                return False
        if ((letter != 'F') & (letter != 'D') & (letter!= 'C')):
            if ((y == 14) & (board[y-2][x] != " _")):
                return False
            elif (y < 14):
                if (board[y+2][x] != " _"):
                    return False

    print ("x: ", end="")
    print (x)
    print ("y: ", end="")
    print (y)
    if (orientation == 1):
        if (letter != 'F'):
            if (board[y][x-1] != " _"):
                return False
        if ((letter != 'F') & (letter != 'D')):
            if (board[y][x+1] != " _"):
                return False
        if((letter != 'F') & (letter != 'D') & (letter!= 'C')):
            if ((x == 6) & (board[y][x - 2] != " _")):
                return False
            if (x < 6):
                if (board[y][x + 2] != " _"):
                    return False
    return True

def get_coordinates_for_ships(player, coordinates_x, coordinates_y):
    for i in range(0,16):
        for j in range(0,8):
            if player[i][j]!=" _":
                coordinates_x.append(i)
                coordinates_y.append(j)
