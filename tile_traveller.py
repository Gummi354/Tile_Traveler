# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
import random

def move(direction, col, row, move_counter):
    ''' Returns updated col, row given the direction '''
    move_counter += 1
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row, move_counter)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2) #Add Coin
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2) Add Coin
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3) Add Coin
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2) Add Coin
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def coins_locations(col, row):
    '''Returns True if the player is in right location given the supplied location'''
    coin_location = False

    if col == 1 and row == 2:
        coin_location = True
    elif col == 2 and row == 2:
        coin_location = True
    elif col == 2 and row == 3:
        coin_location = True
    elif col == 3 and row == 2:
        coin_location = True

    return coin_location

def pull_lever_get_coin(coin_counter):
    '''Returns the updated coin counter and True if the player chooses to Pull the lever given the coin counter '''
    Pull = random.choice( ["y", "n"] )
    print("Pull a lever (y/n):", Pull)
    Pull = Pull.lower()
    Pull_lever = False
    if Pull == 'y':
        coin_counter +=1
        Pull_lever = True
    return coin_counter, Pull_lever
        
def play():
    #seed_amount = input("Input seed: ")
    random.seed( int(input("Input seed: ")) )
    victory = False
    row = 1
    col = 1
    coin_counter = 0
    move_counter = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        direction = random.choice( ["n", "e", "s", "w"] )
        print("Direction:", direction)
        direction = direction.lower()
        
        if not direction in valid_directions:
            print("Not a valid direction!")
            print_directions(valid_directions)
            move_counter += 1
        else:
            col, row, move_counter = move(direction, col, row, move_counter)
            victory = is_victory(col, row)
            if victory:
                print("Victory! Total coins "+str(coin_counter)+". Moves " + str(move_counter) + ".")
            else:
                locating_coins = coins_locations(col, row)
                if locating_coins:
                    coin_counter, Pull_lever = pull_lever_get_coin(coin_counter)
                    if Pull_lever: 
                        print("You received 1 coin, your total is now "+str(coin_counter)+".")
                valid_directions = find_directions(col, row)
                print_directions(valid_directions)

Play_again = True
while Play_again:
    play()
    another_one = input("Play again (y/n): ")
    another_one = another_one.lower()
    if another_one == "n":
        Play_again = False


            