# This software is used to simulate korean style drinking games. The following games are simulated:
#   -> Flick the bottle cap
#   -> Guess the number in the bottle cap
#   -> Titanic
# The code for the games are in external py files, this file is meant to act as a "main function".

# Import Files
import FlickTheCap

# Auxiliary Functions ############################################################################
def GetListOfNames():
    print("Enter Player Names Here (note, seperate values with commas ','):")
    StrOfNames = input()
    ListOfNames = StrOfNames.split(",")
    print("Players are: ")
    print(ListOfNames)
    return ListOfNames

# Test Functions #################################################################################
def TestFlickTheCap(ListOfNames):
    FlickTheCap.FlickTheCap(ListOfNames)

# Main Function ###################################################################################
LoN = GetListOfNames()
TestFlickTheCap(LoN)