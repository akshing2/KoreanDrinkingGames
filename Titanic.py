# This file is used to simulate the Titanic game as part of Korean Drinking Games

# Import Files
import math
from scipy.stats import expon
from random import *

# Auxiliary Functions #################################################################

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
	total = 120
	min = 125
	max = 150
	tipped = False

	while not tipped:
		inputChoice = int(input("\nPlease select a pouring option...\n1. Small Pour\n2. Medium Pour\n3. Heavy Pour\nChoice (1,2,3): "))
		# logic for strength of pour 
		if inputChoice == 1:
			currInput = randint(1,2)
		elif inputChoice == 2:
			currInput = randint(2,5)
		elif inputChoice == 3:
			currInput = randint(5,10)
		perc_full = total/max*100
		total = total + currInput
		print (currInput)
		print("Total is ", total)
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
		print("For glass " ,perc_full, " full")
		print(Chance, "Chance of tipping")

		# From chance percentage determine if cup tips
		x = randint(1, 100)
		print(x)
		if x <= Chance:
		  print("TIP!")
		  tipped = True

Titanic([])