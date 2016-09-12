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
BoardSetupUtilities.get_coordinates_for_ships(player1, ship_x_coordinates_player1, ship_y_coordinates_player1)
BoardSetupUtilities.get_coordinates_for_ships(player2, ship_x_coordinates_player2, ship_y_coordinates_player2)

win = False

GameUtilities.clear_screen()
print("Welcome to Battleships! Press enter to begin!")
temp = input()

# Player 1 goes first.
player = 1

while (win == False):
    GameUtilities.clear_screen()

    print("It's your turn, player", player, "\b!\n")
	
	# Print board, without displaying opposing player's side.
    if (player == 1):
        GameUtilities.print_board(player1, empty)
    else:
        GameUtilities.print_board(empty, player2)

	# Get x co-ordinate from user.
    x = InputUtilities.get_x_input()
    
    if (player == 1):
		
		# Ensure input for player 1 corresponds to right half of board.
        while ((x<7) | (x>15)):
            print("Please input letter between I and P.")
            x = InputUtilities.get_x_input()
    else:
	    
	    # Ensure input for player 2 corresponds to left half of board.
        while ((x<0) | (x>7)):
            print("Please input letter between A and H.")
            x = InputUtilities.get_x_input()
            
    # Get y co-ordinate from user.      
    y = InputUtilities.get_y_input()
    
    GameUtilities.clear_screen()

    if (player == 1):
        GameUtilities.hit_board(x, y, player2)
        win = GameUtilities.check_win(player2, ship_x_coordinates_player2, ship_y_coordinates_player2)
                
        if (win == False):
            print("Player 2 press enter to begin your turn!")
            temp = input()
            player = 2
        else:
            print("\t\t\tPlayer 1 wins!\n")

    else:
        GameUtilities.hit_board(x, y, player1)
        win = GameUtilities.check_win(player1, ship_x_coordinates_player1, ship_y_coordinates_player1)
		
        if (win == False):
            print("Player 1 press enter to begin your turn!")
            temp = input()
            player = 1
        else:
            print("\t\t\tPlayer 2 wins!\n")

#the board is printed with the numbers, letters and the two player's grids placed side by side

GameUtilities.print_board(player1, player2)
