import random
import BoardSetupUtilities
import GameUtilities
import InputUtilities

player1 = []
player2 = []
empty = []

# Board consists of two 2D arrays placed side by side.
# Each 2D array is a grid with dimensions 16x8. You can specify positions within the 2D array to place objects.

ship_x_coordinates_player1=[]
ship_y_coordinates_player1=[]

ship_x_coordinates_player2=[]
ship_y_coordinates_player2=[]

#set up each player's half of the board.
BoardSetupUtilities.set_up_board(player1)
BoardSetupUtilities.set_up_board(player2)
BoardSetupUtilities.set_up_board(empty)

#place ships for player1
BoardSetupUtilities.place_ship(player1, 'F')
BoardSetupUtilities.place_ship(player1, 'D')
BoardSetupUtilities.place_ship(player1, 'C')
BoardSetupUtilities.place_ship(player1, 'B')

#place ships for player2
BoardSetupUtilities.place_ship(player2, 'F')
BoardSetupUtilities.place_ship(player2, 'D')
BoardSetupUtilities.place_ship(player2, 'C')
BoardSetupUtilities.place_ship(player2, 'B')

#get coordinates for ships on board
BoardSetupUtilities.get_coordinates_for_ships(player1,ship_x_coordinates_player1, ship_y_coordinates_player1)
BoardSetupUtilities.get_coordinates_for_ships(player2,ship_x_coordinates_player2, ship_y_coordinates_player2)

#set turn to player1
turn=1

#initialise x and y
x=ord('A')-1
y=-1

win=False
for i in range(0, len(ship_x_coordinates_player1)):
    print (ship_x_coordinates_player1[i], end="")
    print (",", end="")
    print (ship_y_coordinates_player1[i])

#store coordinates for x and y in variables
while(win==0):
    win==GameUtilities.check_win(player1, ship_x_coordinates_player1, ship_y_coordinates_player1)
    GameUtilities.clear_screen()

    print(win)
    if(win==True):
        print ("broken")
        break

    #player1's turn
    GameUtilities.print_board(player1,empty)

    x=InputUtilities.get_x_input(x)

    while ((x<7) | (x>15)):
        print("Please input letter between I and P.")
        x=InputUtilities.get_x_input(x)

    y=get_y_input(y)
    hit_board(x,y,player2)

    win==GameUtilities.check_win(player2, ship_x_coordinates_player2, ship_y_coordinates_player2)
    GameUtilities.clear_screen()

    print(win)
    if(win==True):
        print ("broken")
        break

    #player2's turn
    GameUtilities.print_board(empty,player2)

    x=InputUtilities.get_x_input(x)

    while ((x<0) | (x>7)):
        print("Please input letter between A and H.")
        x=InputUtilities.get_x_input(x)

    y=get_y_input(y)

    hit_board(x,y,player1)

#the board is printed with the numbers, letters and the two player's grids placed side by side.
print ("Both players visible on the board.")
GameUtilities.print_board(player1, player2)

for i in range(0,len(ship_x_coordinates_player1)):
    print (ship_x_coordinates_player1[i], end=" ")
    print ("", end=" ")
    print (ship_y_coordinates_player1[i])

for i in range(0,len(ship_x_coordinates_player2)):
    print (ship_x_coordinates_player2[i], end=" ")
    print ("", end=" ")
    print (ship_y_coordinates_player2[i])
