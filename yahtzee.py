# Yahtzee Game
# inviting programmed players to compete
# Scott Anderson
# Jun 28, 2020

import sys
import random
import scoring as s

import randomplayer as p1
import scott as p2

numGames = 1

players = []

scorecardRows = ["Aces","Twos","Threes","Fours","Fives","Sixes","3OfAKind","4OfAKind","FullHouse","SmStraight","LgStraight","YAHTZEE","Chance"]
nl = "\n"

class player:
	def __init__(self,name,rollDecision,scoreDecision):
		self.name = name
		self.rollDecision = rollDecision
		self.scoreDecision = scoreDecision
		self.currGame = 0
		self.currGameCard = {}
		self.scorecards = {} #dictionary of scorecards - "1":{scorecard object}
	
	def startGame(self,game):
		#create new game card
		self.currGame = game
		self.currGameCard = s.scorecard(game)

	def endGame(self,game):
		finalScore = self.currGameCard.scoreFinal()
		self.scorecards[self.currGame] = self.currGameCard

		#reset values
		self.currGameCard = {}
		self.currGame = 0

		return finalScore


def rolldie():	return random.randint(1,6)

def main(): #game play

	#setup players
	players.append(player(p1.__name__,p1.rollDecision,p1.scoreDecision))
	
	if 'p2' in sys.modules: players.append(player(p2.__name__,p2.rollDecision,p2.scoreDecision))
	if 'p3' in sys.modules: players.append(player(p3.__name__,p3.rollDecision,p3.scoreDecision))
	if 'p4' in sys.modules: players.append(player(p4.__name__,p4.rollDecision,p4.scoreDecision))
	for p in players:
		print (str(p.name))

	numPlayers = len(players)
	bRollDie = [1,1,1,1,1] #boolean array determining which dice to roll

	g=1
	while g<=numGames:
		# 13 turns in a full game
		# 3 rolls per turn
		numTurns = 13
		numRolls = 3

		#start game
		for p in players: p.startGame(g)

		t=1
		while t<=numTurns:
			print ("START TURN " + str(t))
			for p in players: #loop through players
				print("== " + p.name + "'s turn ==")

				r=1
				dice = [0,0,0,0,0] # holder for die roll
				while r<=numRolls:
					#print("== ROLL " + str(r) + " ==" + nl)

					
					if r==1:  #first time, roll all die
						bRollDie = [1,1,1,1,1]
					else: #every other roll, get info from player's rollDecision function
						bRollDie = p.rollDecision(r,dice)

					#print(bRollDie)

					# ROLL DICE - determine new roll values
					for i,d in enumerate(bRollDie):
						if d: dice[i] = rolldie()

					print(" roll " + str(r) + " " + str(dice))

					r += 1

				## TURN COMPLETE
				print(p.name + " turn over")

				scoreRow = p.scoreDecision(dice,p.currGameCard)
				turnScore = s.scorePlay(scoreRow,dice)
				p.currGameCard.setScore(scoreRow,turnScore)
				print("= score " + scoreRow + ": " + str(p.currGameCard.getScoreRow(scoreRow))+" =" + nl)

				############################
				## TESTING
				## run through dice combinations
				#scorecardRows = ["Aces","Twos","Threes","Fours","Fives","Sixes","3OfAKind","4OfAKind","FullHouse","SmStraight","LgStraight","YAHTZEE","Chance"]
				# first 13 rolls, follow this order of items
				# rollCombos = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5],[6,6,6,6,6],[3,3,3,2,1],[4,4,4,4,1],[2,2,3,3,3],[4,3,2,1,6],[6,5,4,3,2],[5,5,5,5,5],[3,5,2,1,2]]
				# dice = rollCombos[r-1]
				# scoreRow = scorecardRows[roll-1] #TESTING
				# rollScore = s.scorePlay(scoreRow,dice) #TESTING
				############################
		
			t +=1 #NEXT TURN



			#TESTING
			# if t>1:
			# 	player1.getScore()
			# 	player1.getGameScores()
			# 	break
		## END GAME
		## Record game data
		for p in players:
			print (p.name + ": " + str(p.endGame(g)))

		g += 1	


if __name__ == '__main__':
	main()