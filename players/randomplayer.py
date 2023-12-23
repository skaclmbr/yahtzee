# Player
# Random Test Player
# Scott Anderson
# 12/23/23
import random
import scoring as s

########################################################################
## Random Player
# chooses roll combination randomly
# scores maximum available row

########################################################################
## Player library must have two functions:
# rollDecision() to deterime which dice to roll (or whether to roll)
# scoreDecision() to determine how to score the turn

## see the scoring library for tools to help with scoring:
# tallydiefaces(dice) retunrns two boolean, six element arrays:
#		"count" - count of die for each die face
#		"sum" - sum of die for each die face
#
# scorePlay (row, dice)
#		returns the score for a given score row and dice combination

def rollDecision(roll,dice):
	#INPUTS:
	#	roll = the roll number (2 or 3)
	#	dice = array of dice values from last roll e.g., [3,2,6,4,1]
	#OUTPUT:
	# 	rollAgain = boolean determining if player should roll again
	#	rollDie = boolean array of dice to roll e.g., [0,0,1,0,0]

	################################################################
	# insert algorithm here - set rollDie to boolean array of dice to roll

	rollDie = []
	f = 1
	while f <= 5:
		# loop through each die face, select random boolean value to roll
		rollDie.append(random.choice([True, False]))
		f += 1
	
	rollAgain = random.choice([True, False])

	# end algorithm
	################################################################

	result = {
		"rollAgain": rollAgain,
		"rollDie": rollDie
	}
	return result

def scoreDecision (dice, scorecard):
	#decide how to score the final roll
	#INPUT:
	#	dice = array of dice values from last roll e.g., [3,2,6,4,1]
	#	scorecard = dictionary of current scorecard
	#OUTPUT:
	#	row = row name to use for score

	################################################################
	#insert algorithm here - set rowChoice variable to scorecard row chosen
	#TESTING
	# for now, selects the blank row with the maximum score value

	#write code here to evaluate and choose the row that results in the highest score

	maxRow = ""
	maxVal = 0

	print(scorecard.card)
	# loop through scorecard
	for r in scorecard.getEmptyRows():

		# calculate the scorecard value
		value = s.scorePlay(r,dice)
		if value > maxVal:
			maxVal = value
			maxRow = r

	rowChoice = maxRow

	#end algorithm
	################################################################

	return rowChoice