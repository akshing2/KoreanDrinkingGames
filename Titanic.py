# This file is used to simulate the Titanic game as part of Korean Drinking Games

# Import Files
import math
from scipy.stats import expon
import time
from random import *
import os

# Auxiliary Functions #################################################################
def DramaticPause(nDrops):
	os.system('clear')
	print("Pouring")
	time.sleep(1)
	for i in range(0, nDrops):
		time.sleep(0.3)
		print("...")
	time.sleep(1)

# Makes the cup Array
def MakeCup():
	cupSlice = [' ',' ',' ','||',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','||']
	cupBase = [' ',' ',' ','||','_','_','_','_','_','_','_','_','_','_','||']
	cup = []
	for i in range(0,16):
		cup.append(cupSlice.copy())
	cup.append(cupBase)
	return cup

# Prints the Cup
def PrintCup(cup):
	os.system('clear')
	print('\n\n\n')
	for cSlice in cup:
		print('\033[1;33;40m '.join(cSlice))

# Fills the cup with a single drop
def FillCupOnce(cup):
	sliceNum = 15
	i = 0
	filled = False
	while not filled:
		if i == 16:
			return cup
		if cup[sliceNum-i].count('#') < 10:
			while not filled:
				randIndex = randint(4,13)
				if cup[sliceNum-i][randIndex] != '#':
					cup[sliceNum-i][randIndex] = '#'
					filled = True
		else:
			i = i + 1
	return cup

# Fills the cup with amount drops while printing
def FillNPrintCup(cup, amount, rate):
	PrintCup(cup)
	time.sleep(1)
	for i in range(0, amount):
		cup = FillCupOnce(cup)
		PrintCup(cup)
		time.sleep(rate)
	time.sleep(1)
	return cup


# Main ################################################################################
def Titanic(ListOfNames):
	data_expon = expon.rvs(scale=1,loc=0,size=10000)

	data = []
	i = 0
	while i < 10.001:
	  data.append(math.exp(i) - math.exp(0))
	  i = i + 0.001
	max_val = data[len(data)-1]

	# max is 150, Input (volume in cup is 0-149 for the sake of indexing)
	# anything <= min has 0 chance of tipping
	# decreasing min increases the effective range of input for tipping
	currInput = 0
	total = 75
	min = 100
	max = 150
	tipped = False
	roundNum = 0

	cup = MakeCup()
	cup = FillNPrintCup(cup, total, 0.02)

	while not tipped:
		print("\033[0;37;40m \n" + ListOfNames[roundNum % len(ListOfNames)], end='')
		inputChoice = int(input(" please select a pouring option...\n1. Small Pour\n2. Medium Pour\n3. Heavy Pour\nChoice (1,2,3): "))
		print()
		# logic for strength of pour 
		if inputChoice == 1:
			currInput = randint(1,2)
			cup = FillNPrintCup(cup, currInput, 2)
		elif inputChoice == 2:
			currInput = randint(2,5)
			cup = FillNPrintCup(cup, currInput, 1)
		elif inputChoice == 3:
			currInput = randint(5,10)
			cup = FillNPrintCup(cup, currInput, 0.5)

		perc_full = total/max*100
		total = total + currInput

		if total > min and total < max:
		  	# The following logic scales the input relative to position between min and max
		  	dif = max - min
		  	delta = total - min
		  	scale_perc = delta/dif  
		  	Chance = data[int(len(data)*scale_perc)]/max_val *100
		elif total > max:
			Chance = 100
		else:
		  	Chance = 0
		#print("For glass " ,perc_full, " full")
		#print(Chance, "Chance of tipping")

		# From chance percentage determine if cup tips
		x = randint(1, 100)
		if x <= Chance:
		  	print("\033[1;31;40m \n\n" + ListOfNames[roundNum % len(ListOfNames)].upper() + " LOST!!!")
		  	tipped = True
		  	return roundNum % len(ListOfNames)

		# Pour more
		print("\033[0;37;40m \n" + ListOfNames[roundNum % len(ListOfNames)], end='')
		inputChoice = input(" would you like to pour some more?\nYes or No (Y/N): ")
		if inputChoice != "Y":
			# Increment Round
			roundNum = roundNum + 1
