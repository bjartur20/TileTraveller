# Authors: Bjartur Þórhallsson, Guðjón Ingi Valdimarsson
# Date: 08.10.2019

# https://github.com/bjartur20/TileTraveller/

'''
1. Calculate which directions are available to the player.
2. Print available directions.
3. Get a direction from the player.
4. Move the player accordingly, if the direction is unavailable ask for a new direction.
6. Repeat until the player's position_int is at 3,1.
7. Print a winning message and close the program.
'''

import random

def get_available_directions (position_int):
    '''
    Generates available positions for the player and returns them as a string of n,s,w or e in a single string.
    Takes in the position_int as an int and returns available directions as a string.
    '''

    pos = position_int
    if pos == 11:
        return "n"
    elif pos == 12:
        return "nes"
    elif pos == 13:
        return "es"
    elif pos == 21:
        return "n"
    elif pos == 22:
        return "sw"
    elif pos == 23:
        return "ew"
    elif pos == 32:
        return "ns"
    elif pos == 33:
        return "sw"
    else:
        print("Error, pos not defined.")

def get_move(position_int, move_count):
    '''
    Asks for input from the user (which direction he chooses to move) and returns the input as a string.
    Takes in the position_int as an int and returns the user's input as a lowercase string.
    '''

    print_available_driections(get_available_directions(position_int))
    user_input_str = get_random_move()
    print ("Direction: {}".format(user_input_str))
    move_count += 1

    while user_input_str not in get_available_directions(position_int):
        print ("Not a valid direction!")
        print_available_driections(get_available_directions(position_int))
        user_input_str = get_random_move()
        print ("Direction: {}".format(user_input_str))
        move_count += 1


    return user_input_str, move_count

def change_position(move_str, position_int):
    '''
        Changes the user position_int based on his input.
        Takes in the user's move as a string and his position_int 
        as an int and returns the user's new position_int as an int.
    '''

    if move_str == "n":
        position_int += 1
    elif move_str == "s":
        position_int -= 1
    elif move_str == "e":
        position_int += 10
    elif move_str == "w":
        position_int -= 10
    else:
        print("Move input not defined")

    return position_int

def get_direction(direction_str):
    '''
    Translates a single character into it's designated direction.
    Takes in a string and returns a string.
    '''

    if direction_str == "n":
        return "(N)orth"
    elif direction_str == "e":
        return "(E)ast"
    elif direction_str == "s":
        return "(S)outh"
    elif direction_str == "w":
        return "(W)est"
    else:
        print ("Error in print_direction")

def print_available_driections(avaialable_directions_str):
    '''
    Prints the available directions which the user can travel in.
    Takes in the available directions as a string and prints directions to the user.
    '''

    if len(avaialable_directions_str) == 1:
        print("You can travel: {}.".format(get_direction(avaialable_directions_str)))
    elif len(avaialable_directions_str) ==  2:
        print("You can travel: {} or {}.".format(get_direction(avaialable_directions_str[0]), get_direction(avaialable_directions_str[1])))
    elif len(avaialable_directions_str) == 3:
        print("You can travel: {} or {} or {}.".format(get_direction(avaialable_directions_str[0]), get_direction(avaialable_directions_str[1]), get_direction(avaialable_directions_str[2])))

def pull_lever(coins_int, position_int):
    ''' Changes the coin value when the user wants to pull a leaver. '''

    lever_list = (12, 22, 23, 32)                                       # Positions of leavers.
    if position_int in lever_list:
        pull_lever_input = get_random_decision()
        print ("Pull a lever (y/n): {}".format(pull_lever_input))       
        if pull_lever_input == "y":                                     # When the user wants to pull a leaver change the coin value.
            coins_int += 1
            print ("You received 1 coin, your total is now {}.".format(coins_int))
    
    return coins_int

def get_random_move():
    ''' Generates a random move. '''

    directions_list = ["n", "e", "s", "w"]
    move = random.choice(directions_list)

    return move

def get_random_decision():
    ''' Generates a random decision for leavers. '''

    decisions_list = ["y", "n"]
    decision = random.choice(decisions_list)

    return decision

def play():
    ''' Plays the game allowing it to be played multiple times, Also holds coin and move values. '''

    position_int = 11                                                   # Initial position
    coins_int = 0
    move_count = 0
    random.seed(int(input("Input seed: ")))
    while position_int != 31:                                           # Runs until the user gets to the end position
        user_move_str, move_count = get_move(position_int, move_count)
        position_int = change_position(user_move_str, position_int)
        coins_int = pull_lever(coins_int, position_int)
    print ("Victory! Total coins {}. Moves {}.".format(coins_int, move_count))
    

def main():
    user_input = "y"
    while user_input == "y":
        play()
        user_input = input("Play again (y/n): ").lower()

main()