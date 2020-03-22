# This file is used to simulate the Flick The Cap game as part of Korean Drinking Games

# Import Files
import random
import time

# Auxiliary Functions #################################################################

# Generate strength of bottle cap
def BottleCapStrength():
    min = 400
    max = 700
    random.seed(1)
    bc_stren = random.randint(min, max)

    return abs(bc_stren)


# Generate strength of flick
def FlickStrength():
    min = 300
    max = 400
    min_flick = 0.1
    max_flick = 0.2

    random.seed(1)
    val = random.random()
    flick_multi = min_flick + (val*(max_flick - min_flick))
    flick_stren = flick_multi*random.randint(min, max)

    return abs(flick_stren)

# Generate graphic of bottle cap
def DrawBottleCap(bc_stren, num_flicks, lean_left):
    ll = lean_left

    height  = 5
    num_tab = 7
    char_per_tab = 3
    num_char = char_per_tab*num_tab
    width = 2*num_char + num_tab
    if bc_stren >= 0:
        # draw the tail bit
        for i in range(0, num_tab):
            print(width*" " + i*" "*ll + (num_tab-i)*" "*(not(ll)) + "*")


    # draw bottle cap with no tail. ie Game End
    for i in range(1, height):
        print("|" + num_tab*"\t" + "|")
    
    print("|" + num_char*"_" + "|")
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
    wait_time = 0.75
    # Get the bottle cap strength
    bc_strength = BottleCapStrength()

    # number of flicks occured
    num_flicks = 0

    # lean of the bottle cap
    lean_left = True

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
        
        # get flick strength
        flick_strength = FlickStrength()
        bc_strength = bc_strength - flick_strength
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