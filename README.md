# KoreanDrinkingGames
A simulation of various Korean Drinking Games using command line interface.

# Instructions
## Setting up players
The game will ask for the names of players as a single string input. List the names
of the players as a single string seperated by commas (","). For example:
'<Name0,Name1,Name2,...NameN>'.

## Flick the cap
In this game, players will simulate "flicking the tail of the cap" off. The number of flicks required to 
flick the cap off is randomly generated, as well as a chance of missing the flick. The winner will flick 
the tail off, and the players either side of them will have to drink. Their loss is added to the scoreboard.

## Higher or Lower
In this game, the winner of "Flick the cap" will decide a number between 0 and 99 inclusive. Other players
take turns guessing the value selected, and if the value is wrong, the winner of "flick the cap" will will 
say "higher", as in the number guessed was lower than the actual number, or "lower" if the opposite is true.
The minimum and maximum guessing ranges are updated accordingly until a player selects the right number. When
this occurs, they lose the game and have to drink. 
