# Yahtzee Game
# inviting programmed players to compete
# Scott Anderson
# Jun 28, 2020
# v0.01 - not functional yet!

import sys
import random
import scoring as s
import json

# define players by pointing to python script defining behavior
import players.randomplayer as p1
import players.scott as p2

# import player3 as p3
# import player4 as p4

players = []

nl = "\n"

class player:
	def __init__(self,name,rollDecision,scoreDecision):
		self.name = name
		self.rollDecision = rollDecision
		self.scoreDecision = scoreDecision
		self.currGameNum = 0
		self.currGameCard = {}
		self.scorecards = [] #list of scorecards - {scorecard object}
	
	def startNewGame(self,gameNum, game):
		#create new game card
		self.currGameNum = gameNum # number of the game
		self.currGameCard = game

	def getCurrGameCard(self):
		return self.currGameCard

	def endGame(self):
		finalScore = self.currGameCard.scoreFinal()
		self.scorecards.append(self.currGameCard.card)

		#reset values
		self.currGameCard = {}
		self.currGameNum += 1

		return finalScore


def rolldie():	return random.randint(1,6)

def main(): #game play

	#setup players
	players.append(
		player(
			p1.__name__,
			p1.rollDecision,
			p1.scoreDecision
			)
		)
	
	if 'p2' in sys.modules: players.append(
		player(
			p2.__name__,
			p2.rollDecision,
			p2.scoreDecision
			)
		)

	if 'p3' in sys.modules: players.append(
		player(
			p3.__name__,
			p3.rollDecision,
			p3.scoreDecision
			)
		)

	if 'p4' in sys.modules: players.append(
		player(
			p4.__name__,
			p4.rollDecision,
			p4.scoreDecision
			)
		)

	for p in players:
		print (str(p.name))
		print(p.scorecards)


	numPlayers = len(players)
	bRollDie = [1,1,1,1,1] #boolean array determining which dice to roll
	numGames = 10
	g=1
	while g<=numGames:
		# 13 turns in a full game
		# 3 rolls per turn
		numTurns = 13
		numRolls = 3

		#start game
		for p in players: 
			p.startNewGame(g, s.scorecard(g))

		t=1
		while t<=numTurns:
			print ("START TURN " + str(t))
			for p in players: #loop through players
				print("== " + p.name + "'s turn ==")

				r=1

				# holder for die roll
				# 0 values mean no roll
				dice = [0,0,0,0,0] 
				while r <= numRolls:
					
					# GET ROLL DECISION
					if r == 1:  #first time, roll all die
						bRollDie = [True,True,True,True,True]

					else: #all other rolls, get info from player's rollDecision function

						rollDecision = p.rollDecision(r, dice)
						if rollDecision["rollAgain"]: # roll again
							bRollDie = rollDecision["rollDie"]

						else: # done rolling, break out of loop
							break

					# ROLL DICE - determine new roll values
					for i,d in enumerate(bRollDie):
						if d: dice[i] = rolldie()

					# TESTING
					# use to fix dice combination for testing
					# dice = [1,1,1,1,2]
					# END TESTING

					print(" roll " + str(r) + " " + str(dice))

					r += 1

				scoreRow = p.scoreDecision(dice, p.currGameCard)
				turnScore = s.scorePlay(scoreRow, dice)
				p.currGameCard.setScore(scoreRow, turnScore)

				print(
					"= score " + 
					scoreRow + 
					": " + 
					str(p.currGameCard.getScoreRow(scoreRow))+
					" =" + 
					nl
					)

				## TURN COMPLETE
				print(p.name + " turn over")

		
			t +=1 #NEXT TURN


		## END GAME
		## Record game data
		for p in players:
			print(p.currGameCard.getScore(p.name))
			print (p.name + "'s final score: " + str(p.endGame()))

		g += 1	

	## CALCULATE FINAL AVERAGE SCORES
	# calculate final stats
	for p in players:
		sumFinalScore = 0
		numGames = 0
		for g in p.scorecards:

			sumFinalScore += g["final"]
			numGames +=1

		avgFinalScore = sumFinalScore/numGames

		print("== Player: " + p.name + " ==")
		print("avg final score: " + str(avgFinalScore))

if __name__ == '__main__':
	main()