import random

player1 = [];
player2 = [];
empty = [];

ship_x_coordinates_player1=[]
ship_y_coordinates_player1=[]

ship_x_coordinates_player2=[]
ship_y_coordinates_player2=[]

# Board consists of two 2D arrays placed side by side.
# Each 2D array is a grid with dimensions 16x8. You can specify positions within the 2D array to place objects.
# A 2D array is a list where every element is also a list.
def set_up_board(player):
    for i in range (0, 16):
        player.append([]); ##create an empty list in every element of the player list.

    for i in range (0, 16):
        for j in range (0,8):
            player[i].append(" _"); #go through every element and assign " _"

def clear_screen():
    for i in range(0,30):
        print ()
# In this function we print out the board, taking each of the two lists as arguments.
# When printing we go through each line of the whole board and print the two player's lists side by side.
def print_board(player1, player2):
    print (" ", end=" ");

    #This part of the code is used to print out the letters on the board.
    c=0;
    for i in range (0, 16):
        print (end="  ");
        print (chr(ord('A')+c), end=" ");
        c=c+1;

    print ();

    #This part of the code is used to print the numbers on the board.
    c=0;
    d=0;
    num = 1;
    for i in range (0, 16):
        if(num<10):
            print (end=" ");
            print (chr(ord('1')+c), end=" ");
            c=c+1;
            if(num<11):
                num=num+1;
        if(num>10):
            print ('1', end="");
            print (chr(ord('0')+d), end=" ");
            d=d+1;
            num=num+1;

        if(num==10):
            num=num+1;

        # This part of the code prints a line from player1's list
        for j in range (0,8):
            print (player1[i][j], end="  ");
        #This part of the code prints a line from player2's list
        for k in range (0,8):
            print (player2[i][k], end="  ");

        # We use the print function here with no arguments to go to a new line before printing the next line of the board.
        print ();

# This function returns either the number 0 or 1. Which ever number is returned will be used to randomly choose if the ships are horizontal or vertical.
def vertical_or_horizontal():
    value = random.randint(0,1);
    if value==0:
        return 0;
    if value==1:
        return 1;

def place_ship(board, letter):
    # randomise coordinates
    x=random.randint(0,7);
    y=random.randint(0,15);
    #randomise whether ship is horizontal or vertical
    position=vertical_or_horizontal(); #vertical = 0, horizontal = 1

    if((position==0)):
        #if center of ship is at top row or bottom row of board move it so it can fit.
        if(y==0):
            y=1;
        if(y==15):
            y=14;

        board[y][x]= " " + letter;

        if((letter != 'F')):
            board[y-1][x]= " " + letter;
        if((letter != 'F') & (letter != 'D')):
            board[y+1][x]= " " + letter;
        if((letter != 'F') & (letter != 'D') & (letter!= 'C')):
            if(y==14):
                board[y-2][x]= " " + letter;
            elif(y==1):
                board[y+2][x]= " " + letter;
            else:
                board[y+2][x]= " " + letter;

    if(position==1):
        #if center of ship is at top column or bottom column of board move it so it can fit.
        if (x==0):
            x=1;
        if (x==7):
            x=6;

        board[y][x]= " " + letter;
        if(letter != 'F'):
            board[y][x-1]= " " + letter;

        if((letter != 'F') & (letter != 'D')):
            board[y][x+1]= " " + letter;
        if((letter != 'F') & (letter != 'D') & (letter!= 'C')):
            if (x>1):
                board[y][x-2]= " " + letter;
            if (x==1):
                board[y][x+2]= " " + letter;

def get_x_input(coordinate):
    c = ord(input("Input value for x: "))

    while((c<(ord('A'))) | (c>(ord('P')))):
        print("Please input letter between 'A' and 'K'")
        c = ord(input("Input value for x: "))

    return c-65;

def get_y_input(coordinate):
    c = int(input("Input value for y: "))

    print(c)
    while((c<1) | (c>16)):
        print("Please input number between 1 and 16")
        c = int(input("Input value for y: "))

    return c-1

def hit_board(x,y,board):
    # print ("x: ")
    # print(x)
    # print ("y: ")
    # print(y)
    if(x>7):
        x=x-8

    board[y][x]=' X'

def get_coordinates_for_ships(player, coordinates_x, coordinates_y):
    for i in range(0,16):
        for j in range(0,8):
            if player[i][j]!=" _":
                coordinates_x.append(i)
                coordinates_y.append(j)

def check_win(player,coordinates_x, coordinates_y):
    win=False
    for i in range (0,len(coordinates_x)):
        if player[coordinates_x[i]][coordinates_y[i]]!=" X":
            print (coordinates_x[i])
            print (coordinates_y[i])
            win=False

    print (win)
    return win

#set up each player's half of the board.
set_up_board(player1);
set_up_board(player2);
set_up_board(empty);

#place ships for player1
place_ship(player1, 'F');
# place_ship(player1, 'D');
# place_ship(player1, 'C');
# place_ship(player1, 'B');

#place ships for player2
place_ship(player2, 'F');
# place_ship(player2, 'D');
# place_ship(player2, 'C');
# place_ship(player2, 'B');

#get coordinates for ships on board
get_coordinates_for_ships(player1,ship_x_coordinates_player1, ship_y_coordinates_player1)
get_coordinates_for_ships(player2,ship_x_coordinates_player2, ship_y_coordinates_player2)

#set turn to player1
turn=1

#initialise x and y
x=ord('A')-1
y=-1

win=False
for i in range(0,len(ship_x_coordinates_player1)):
    print (ship_x_coordinates_player1[i], end=" ")
    print ("", end=" ")
    print (ship_y_coordinates_player1[i])
#store coordinates for x and y in variables
while(win==0):
    win==check_win(player1, ship_x_coordinates_player1, ship_y_coordinates_player1)
    clear_screen()

    print(win)
    if(win==True):
        print ("broken")
        break

    #player1's turn
    print_board(player1,empty)

    x=get_x_input(x);

    while ((x<7) | (x>15)):
        print("Please input letter between I and P.")
        x=get_x_input(x)

    y=get_y_input(y)
    hit_board(x,y,player2)

    win==check_win(player2, ship_x_coordinates_player2, ship_y_coordinates_player2)
    clear_screen()

    print(win)
    if(win==True):
        print ("broken")
        break

    #player2's turn
    print_board(empty,player2)

    x=get_x_input(x)

    while ((x<0) | (x>7)):
        print("Please input letter between A and H.")
        x=get_x_input(x)

    y=get_y_input(y)

    hit_board(x,y,player1)

#the board is printed with the numbers, letters and the two player's grids placed side by side.
print ("Both players visible on the board.")
print_board(player1, player2)

for i in range(0,len(ship_x_coordinates_player1)):
    print (ship_x_coordinates_player1[i], end=" ")
    print ("", end=" ")
    print (ship_y_coordinates_player1[i])

for i in range(0,len(ship_x_coordinates_player2)):
    print (ship_x_coordinates_player2[i], end=" ")
    print ("", end=" ")
    print (ship_y_coordinates_player2[i])