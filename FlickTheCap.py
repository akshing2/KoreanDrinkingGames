# This file is used to simulate the Flick The Cap game as part of Korean Drinking Games

# Import Files
import random
import time
import numpy as np

# Auxiliary Functions #################################################################

# Generate strength of bottle cap
def BottleCapStrength():
    min = 1
    max = 25

    seed_val = random.randint(1, 1000)
    np.random.seed(seed_val)
    bc_stren = np.random.uniform(min, max)

    return abs(bc_stren)


# Generate strength of flick
def FlickStrength():
    min = 0
    max = 400
    min_flick = 0.1
    max_flick = 0.9

    seed_val = int(np.random.uniform(1, 100))
    np.random.seed(seed_val)
    flick_multi = np.random.uniform(min_flick, max_flick)
    flick_stren = flick_multi*np.random.uniform(min, max)

    return abs(flick_stren)

# Generate graphic of bottle cap
def DrawBottleCap(bc_stren, num_flicks, lean_left):
    ll = lean_left

    height  = 5
    num_tab = 3
    char_per_tab = 8
    num_char = char_per_tab*num_tab
    width = 2 + num_tab*num_char
    if bc_stren >= 0:
        # draw the tail bit
        for i in range(0, height):
            print((width-i)*" "*ll + i*" "*(not(ll)) + "*")

    # draw bottle cap with no tail. ie Game End
    for i in range(0, height):
        print("|" + num_tab*"\t" + "|")
    
    print("|" + (num_char-1)*"_" + "|")
    print("Number of Flicks = " + str(num_flicks))
    
    # switch lean left
    ll = not(ll)

    return ll

    # Main function #######################################################################
def FlickTheCap(ListOfNames):
    game_fin = False
    max_players = len(ListOfNames)
    player = 0
    winner = "UNKOWN ERROR"
    wait_time = 0.65
    # Get the bottle cap strength
    bc_strength = BottleCapStrength()

    # number of flicks occured
    num_flicks = 0

    # lean of the bottle cap
    lean_left = True
    print()
    print()
    print("########## FLICK THE BOTTLE CAP ##########")
    print()
    # main game loop
    while game_fin == False:
        # get player to play
        print("Your turn, " + ListOfNames[player] + "!")
        print("Press ENTER to flick!")
        input()
        
        print("Simulating Flick")
        for i in range (0, 3):
            time.sleep(wait_time)
            print("...")
        
        # Extra lines to separate drawing
        print()
        print()
        # get flick strength
        flick_strength = FlickStrength()
        bc_strength = bc_strength - 1   # working with random number of flicks
        num_flicks = num_flicks + 1
        # draw bottle cap state
        lean_left = DrawBottleCap(bc_stren=bc_strength, num_flicks=num_flicks, lean_left=lean_left)

        # check for winner
        if bc_strength <= 0:
            print("Congratulations, " + ListOfNames[player] + "!")
            winner = ListOfNames[player]
            game_fin = True

        # otherwise, go to next player
        player = player + 1
        if player > (max_players - 1):
            player = 0
        

    return winner