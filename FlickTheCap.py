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
    max = 1

    seed_val = int(np.random.uniform(1, 100))
    np.random.seed(seed_val)
    flick_stren = np.random.uniform(min, max)

    return abs(flick_stren)

# Generate graphic of bottle cap
def DrawBottleCap(bc_stren, bc_init, num_flicks, lean_left, flick_success):
    ll = lean_left

    height  = 4
    num_tab = 3
    char_per_tab = 8
    num_char = char_per_tab*num_tab
    width = 2 + num_tab*num_char

    # simulating flick miss here
    if not(flick_success):
        print("WOOPS, YA MISSED\n")
        ll = not(ll)

    if bc_stren >= 0:
        # draw the tail bit
        # for i in reversed(range(0, height)):
        #     print((num_char-i)*" "*ll + i*" "*(not(ll)) + "*")
        # I'm ashamed of what I'm doing here
        num_del = 5
        if ll:
            print("*")
            print("     *")
            print("             *")
            print("                     *")
            print("                           *")
        else:
            print(" " + num_tab*"\t" + "                             *")
            print(" " + num_tab*"\t" + "                     *")
            print(" " + num_tab*"\t" + "             *")
            print(" " + num_tab*"\t" + "     *")
            print(" " + num_tab*"\t" + "*")

    # draw bottle cap with no tail. ie Game End
    for i in range(0, height):
        print("|" + num_tab*"\t" + "|")
    
    print("|" + (num_char-1)*"_" + "|")
    print("\n Number of Flicks = " + str(num_flicks) + "\n")

    # now let them know how much damage has been done
    low_damage = [0.67*bc_init, 1.0*bc_init]
    mod_damage = [0.34*bc_init, 0.66*bc_init]
    high_damage = [0*bc_init, 0.33*bc_init]

    if low_damage[0] <= bc_stren <= low_damage[1]:
        print("The cap's barely moved! Surely you can do more damage!\n")
    elif mod_damage[0] <= bc_stren <= mod_damage[1]:
        print("Hmmm, the cap is breaking but I think you can put more oomf in it...\n")
    elif high_damage[0] <= bc_stren <= high_damage[1]:
        print("You almost got it! Just a few more taps now!\n")
    
    # switch lean left
    ll = not(ll)

    return ll

    # Main function #######################################################################
def FlickTheCap(ListOfNames):
    game_fin = False
    max_players = len(ListOfNames)
    player = 0
    winner = player
    ret = dict()
    ret["WINNER"] = "UNKOWN ERROR"
    wait_time = 0.65
    # Get the bottle cap strength
    bc_strength = BottleCapStrength()
    bc_init = bc_strength
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
        flick_success = False
        flick_strength = FlickStrength()
        if flick_strength >= 0.33:
            # successfull flick
            bc_strength = bc_strength - 1
            flick_success = True

        num_flicks = num_flicks + 1   # working with random number of flicks
        
        # draw bottle cap state
        lean_left = DrawBottleCap(bc_stren=bc_strength, bc_init=bc_init, num_flicks=num_flicks, lean_left=lean_left, flick_success=flick_success)

        # check for winner
        if bc_strength <= 0:
            print("Congratulations, " + ListOfNames[player] + "!")
            print("Following players need to DRINK:")
            winner = player
            ret["WINNER"] = winner
            
            # get losers
            loser1 = winner - 1
            if loser1 < 0:
                loser1 = max_players - 1
            loser2 = winner + 1
            if loser2 > (max_players - 1):
                loser2 = 0

            ret["LOSER1"] = loser1
            ret["LOSER2"] = loser2
            ret["LOSERS"] = [loser1, loser2]
            print(ListOfNames[loser1])
            print(ListOfNames[loser2])
            game_fin = True

        # otherwise, go to next player
        player = player + 1
        if player > (max_players - 1):
            player = 0
        

    return ret