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

def get_available_directions (position):
    return available_directions

def get_move(position, available_directions):
    return move

def change_position(move, position):
    return position

def print_available_driections(avaialable_directions):
    print()


def main():
    position = 11
    while position != 31:
        available_moves = get_available_directions(position)
        print_available_driections(available_moves)
        user_move = get_move(position, available_moves)
        position = change_position(user_move, position)
