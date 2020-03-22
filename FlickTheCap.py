# This file is used to simulate the Flick The Cap game as part of Korean Drinking Games

# Import Files
import random
import time

# Main function #######################################################################
def FlickTheCap(ListOfNames):
    game_fin = False
    max_players = len(ListOfNames)
    player = 0
    winner = "UNKOWN ERROR"
    # Get the bottle cap strength
    bc_strength = BottleCapStrength()

    # number of flicks occured
    num_flicks = 0

    # main game loop
    while game_fin == False:
        # get player to play
        print("Your turn, " + ListOfNames[player] + "!")
        
        print("Simulating Flick")
        for i in range (0, 3):
            time.sleep(0.1)
            print("...")
        
        # get flick strength
        flick_strength = FlickStrength()
        bc_strength = bc_strength - flick_strength
        num_flicks = num_flicks + 1
        # draw bottle cap state

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

# Auxiliary Functions #################################################################

# Generate strength of bottle cap
def BottleCapStrength():
    min = 100
    max = 300
    random.seed(1)
    bc_stren = random.randint(min, max)

    return abs(bc_stren)


# Generate strength of flick
def FlickStrength():
    min = 100
    max = 300
    min_flick = 0.1
    max_flick = 0.5

    val = random.random()
    flick_multi = min_flick + (val*(max_flick - min_flick))
    flick_stren = flick_multi*random.randint(min, max)

    return abs(flick_stren)

# Generate graphic of bottle cap