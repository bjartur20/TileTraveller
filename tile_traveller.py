# Authors: Bjartur Þórhallsson, Guðjón Ingi Valdimarsson
# Date: 17.09.2019

'''
1. Calculate which directions are available to the player.
2. Print available directions.
3. Get a direction from the player.
4. Move the player accordingly, if the direction is unavailable ask for a new direction.
6. Repeat until the player's position is at 3,1.
7. Print a winning message and close the program.
'''

def get_available_directions (pos):
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

def get_move(position):
    user_input = input("Direction: ").lower()

    while user_input not in get_available_directions(position):
        print ("Not a valid direction!")
        user_input = input("Direction: ").lower()

    return user_input

def change_position(move, position):
    if move == "n":
        position += 1
    elif move == "s":
        position -= 1
    elif move == "a":
        position += 10
    elif move == "w":
        position -= 10
    else:
        print("Move input not defined")

    return position

def print_direction(direction_str):
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

def print_available_driections(avaialable_directions):
    print()


def main():
    position = 11
    while position != 31:
        available_moves = get_available_directions(position)
        print_available_driections(available_moves)
        user_move = get_move(position)
        position = change_position(user_move, position)

main()