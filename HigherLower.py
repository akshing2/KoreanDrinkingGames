def HigherLower(ListOfNames, winner_id):
    print("########## HIGHER/LOWER ##########")

    print(ListOfNames[winner_id] + " You must select a random number between 0 and 99 inclusive")

    # main game loop
    quit  = False
    player_id = 0
    while quit == False:
        if player_id == winner_id:
            player_id += 1
            continue # skip if it's on winner
        
        print("Player: " + ListOfNames[player_id] + ", guess the number")
        print("Were you right? (y/n)")

        ch = input()

        if ch is "y":
            loser_id = player_id
            # print lose statement
            print("DRINK!")
            quit = True

        player_id += 1
        if player_id > (len(ListOfNames) - 1):
            player_id = 0
    
    return [loser_id]