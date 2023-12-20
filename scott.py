# Player
# Test Player
# Scott Anderson
# 6/28/20
import random
import scoring

def rollDecision(roll,dice):
	#INPUTS:
	#	roll = the rolls completed (2 or 3)
	#	dice = array of dice values from last roll e.g., [3,2,6,4,1]
	#OUTPUT:
	#	rollDie = boolean array of dice to roll e.g., [0,0,1,0,0]

	################################################################
	# insert algorithm here - set rollDie to boolean array of dice to roll
	#TESTING
	# rollDie = [0,0,1,0,0]
	rollDie = [1,1,1,1,1]

	# end algorithm
	################################################################


	return rollDie

def scoreDecision (dice, scorecard):
	#decide how to score the final roll
	#INPUT:
	#	dice = array of dice values from last roll e.g., [3,2,6,4,1]
	#	scorecard = dictionary of current scorecard
	#OUTPUT:
	#	row = row to use for score

	################################################################
	#insert algorithm here - set rowChoice variable to scorecard row chosen
	#TESTING
	scorecardRows = ["Aces","Twos","Threes","Fours","Fives","Sixes","3OfAKind","4OfAKind","FullHouse","SmStraight","LgStraight","YAHTZEE","Chance"]
	rowItem = random.randint(0,12)
	rowChoice = scorecardRows[rowItem]


	#end algorithm
	################################################################

	return rowChoice
