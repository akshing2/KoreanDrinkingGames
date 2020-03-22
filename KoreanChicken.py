# This software is used to simulate korean style drinking games. The following games are simulated:
#   -> Flick the bottle cap
#   -> Guess the number in the bottle cap
#   -> Titanic
# The code for the games are in external py files, this file is meant to act as a "main function".

# Import Files
import FlickTheCap
import numpy as np

# Auxiliary Functions ############################################################################
def GetListOfNames():
    print("Enter Player Names Here (note, seperate values with commas ','):")
    StrOfNames = input()
    ListOfNames = StrOfNames.split(",")
    print("Players are: ")
    print(ListOfNames)
    return ListOfNames

def UpdateLoserScores(array_of_loser_id, og_loser_scores):
    loser_scores = og_loser_scores
    for i in range(0, (len(array_of_loser_id))):
        loser_id = array_of_loser_id[i]
        loser_scores[loser_id] = loser_scores[loser_id] + 1

    return loser_scores  

def PrintLoserScore(player_names, loser_scores):
    player_str =    "Names: "
    score_str =     "Lost:  "

    for i in range(0, (len(player_names))):
        player_str += player_names[i] + "\t"
        score_str += str(loser_scores[i]) + "\t"
    
    print("\n" + "THE SCORE SO FAR")
    print(player_str)
    print(score_str + "\n")

# Test Functions #################################################################################
def TestFlickTheCap(ListOfNames):
    quit = False
    while not(quit):
        FlickTheCap.FlickTheCap(ListOfNames)
        print("Another Game (y/n)?")
        ch = input()
        if ch is "n":
            quit = True
    

# Main Function ###################################################################################
quit = False
LoN = GetListOfNames()

#initialise loser scoreboard
loser_scores =  np.zeros(len(LoN))

while not(quit):
    # print loser scores
    PrintLoserScore(LoN, loser_scores)

    ret = FlickTheCap.FlickTheCap(LoN)
    loser_array = [ret["LOSER1"], ret["LOSER2"]]
    # update loser scores
    loser_scores = UpdateLoserScores(ret["LOSERS"], loser_scores)

    # print loser scores
    PrintLoserScore(LoN, loser_scores)

    print("New Round? (y/n)")
    ch = input()
    if ch is "n":
        quit = True

