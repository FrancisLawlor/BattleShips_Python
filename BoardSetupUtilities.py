import os

def set_up_board(player):
    for i in range (0, 16):
        player.append([]) # Create an empty list in every element of the player list.

    for i in range (0, 16):
        for j in range (0,8):
            player[i].append(" _") # Go through every element and assign " _"

def clear_screen():
	os.system('clear')
