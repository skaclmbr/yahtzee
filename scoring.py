# Yahtzee Scoring
# library for calculating scores for passed arrays of Yahtzee dice values
# Scott Anderson
# 6/29/20


scorecardRows = [
	"Aces",
	"Twos",
	"Threes",
	"Fours",
	"Fives",
	"Sixes",
	"3OfAKind",
	"4OfAKind",
	"FullHouse",
	"SmStraight",
	"LgStraight",
	"YAHTZEE",
	"Chance"
	]

ssPatterns = [[1,1,1,1,0,0],[0,1,1,1,1,0],[0,0,1,1,1,1]]
lsPatterns = [[1,1,1,1,1,0],[0,1,1,1,1,1]]

class scorecard:
	def __init__(self,g):
		#pass game number
		self.game = g
		self.card = {} #dicationary for storing card scores
		
		#setup scorecard rows
		for r in scorecardRows:	self.card[r]="NA"

	def emptyRow(self,row):
		if row:
			#check to see if score already filled
			rowStatus = False
			#print (row + ": " + str(self.card[row]))
			# print(str(self.card))
			if self.card[row]=="NA": rowStatus = True

			return rowStatus

	def getScoreRow(self,row):
		# print("get score row: " + str(row))
		if row:
			return self.card[row]

	def getScore(self):

		#print current scorecard
		print("== " + self.name + " Scorecard ==")
		for r,v in self.card.items():
			print(r+": " + str(v) +nl)


	def setScore(self,row,score):
		msg = "Scored " + str(score) + " in " + row
		if self.emptyRow(row):
			self.card[row] = score
		else:
			#already used
			msg = "Row already used."

		print(msg)

	def addGameScores(self,score):
		#tally scorecard and add
		self.gameScores.push(score)

	def getGameScores(self):
		#tally scorecard and add
		return self.gameScores


	def scoreFinal(self):
		#adds up scorecard
		## INSERT CODE HERE TO CALCULATE FINAL SCORE
		score = 10

		#Add score to array
		self.card["final"] = score
		return score 
	

def checkPattern(bFacesArray,cFaces):
	#compare a boolean and count array of dice values
	#boolean array expresses the pattern that must be true
	#INPUT:
	#	bFacesArray = array of boolean arrays of acceptable face pattern
	#	cFaces = array with count of number of each face (1-6) 
	#RETURN:
	#	False or Score Value
	#cFaces = [3,0,0,1,1,0] #count of face values [1,1,1,4,5]
	passes = True
	for x in bFacesArray:
		for i,v in enumerate(x):
			if v and not cFaces[i]: passes = False


def tallyDieFaces(dice):
	# diceFaces = {1:0,2:0,3:0,4:0,5:0,6:0} #dictionary to tally number of face values in each
	countFaces = [0,0,0,0,0,0] #dictionary to tally number of face values in each
	sumFaces = [0,0,0,0,0,0] #dictionary to tally number of face values in each

	#loop through dice values
	for i,d in enumerate(dice):	
		countFaces[d-1] +=1
		sumFaces[d-1] +=d

	return {"count":countFaces,"sum":sumFaces}

def scorePlay(row, dice):
	#takes array of dice and selected row, determines score
	#INPUT:
	#	row = row in which to score the dice
	#	dice = array of 5 dice values to score
	#OUTPUT:
	#	returns point value

	#reference:
	#scorecardRows = ["Aces","Twos","Threes","Fours","Fives","Sixes","3OfAKind","4OfAKind","FullHouse","SmStraight","LgStraight","YAHTZEE","Chance"]
	# calculate scoring for passed cateogry on dice array
	# if not valid (e.g., not a Full House) = fill scorecard row with 0
	#diceFaces = {1:0,2:0,3:0,4:0,5:0,6:0} #dictionary to tally number of face values in each
	tdf = tallyDieFaces(dice)
	diceFaceCount = tdf["count"]
	diceFaceSum = tdf["sum"]
	faceSum = 0
	passes = False
	score = 0

	# print(diceFaceCount)
	# print(diceFaceSum)
	if row=="Aces":
		score = diceFaceSum[0]
	elif row=="Twos":
		score = diceFaceSum[1]

	elif row=="Threes":
		score = diceFaceSum[2]

	elif row=="Fours":
		score = diceFaceSum[3]

	elif row=="Fives":
		score = diceFaceSum[4]

	elif row=="Sixes":
		score = diceFaceSum[5]

	elif row=="3OfAKind":
		for i,d in enumerate(diceFaceCount):
			if d>=3:passes = True
			faceSum += diceFaceSum[i]

		if passes:
			score = faceSum

	elif row=="4OfAKind":
		for i,d in enumerate(diceFaceCount):
			if d>=4:passes = True
			faceSum += diceFaceSum[i]

		if passes:
			score = faceSum

	elif row=="FullHouse":
		three = False
		two = False
		for i,d in enumerate(diceFaceCount):
			if d==3:three = True
			if d==2:two = True

		if two and three: passes = True

		if passes:
			score = 25

	elif row=="SmStraight":
		passes = checkPattern(ssPatterns,diceFaceCount)

		if passes:
			score = 30

	elif row=="LgStraight":
		passes = checkPattern(lsPatterns,diceFaceCount)

		if passes:
			score = 40

	elif row=="YAHTZEE":
		for i,d in enumerate(diceFaceCount):
			if d==5: passes = True

		if passes: score = 50

	elif row=="Chance":
		for i,d in enumerate(diceFaceCount):
			faceSum += diceFaceSum[i]

		score = faceSum

	else:
		pass

	return score