#Marty Rudolf DeGroot.py

from sympy import * # sympy only working when using wildcard import
import numpy as np
from numpy.linalg import norm
init_printing(use_unicode = True)

class DeGroot:
	"""DeGroot learning for finding consensus beliefs from steady groups."""

	def __init__(self, pastVote, currentVote):
		"""Constructor for DeGroot class.

		Imported packages:
		sympy, numpy(np)

		Keyword arguments:
		pastVote -- 2D ndarray of votes made by group members in the past with people changing
			row-wise and choices changing column-wise
		currentVote -- 2D ndarray of votes made by group members to get current results with
			people changing row-wise and choices changing column-wise
		"""

		self.pastVote = pastVote
		self.currentVote = currentVote


		self.numPeople = np.size(pastVote[:, 0])
		self.numPastChoices = np.size(pastVote[0, :])
		self.numCurrentChoices = np.size(currentVote[0, :])

		self.similarities = np.zeros((self.numPeople, self.numPeople,))		
		self.trust = np.zeros((self.numPeople, self.numPeople,))

		self.influence = []

		self.futureChoice = np.empty((self.numPastChoices,)) 
		(self.futureChoice)[:] = np.zeros(self.numCurrentChoices)

	def findSimilarities(self):
		""" Find matrix of similarities between all members of group. 
			Or, how similarly each person votes to each other person.
		"""
		for i in range(self.numPeople):
			for j in range(i, (self.numPeople)):
				personA = (self.pastVote)[i, :]
				personB = (self.pastVote)[j, :]
				distAB = norm(personA - personB)
				self.similarities[i, j] = distAB
				self.similarities[j, i] = distAB

	def findTrust(self):
		""" Find matrix of trust between all members of group.
		 	Or, how similar one person is to the each other person relative to how similar they are
		 	to everybody.
		"""
		for i in range(self.numPeople):
			row = self.similarities[i, :]
			rowSum = np.sum(row)
			for j in range(self.numPeople):
				self.trust[i, j] = self.similarities[i, j] / rowSum

	def getInfluence(self):
		"""Get each group members proportional influence in the group using Markov chain."""
		t = Symbol('t', positive = True)
		
		sympyTrust = Matrix(self.trust)
		P, D = (sympyTrust).diagonalize()
		Dt = (abs(D))**t
		# Trust will converge with time.
		limDt = Dt.limit(t, oo)
		limTt = P * limDt * (P**-1)
		resultInfluence = np.array(limTt).astype(np.float64)
		self.influence = resultInfluence[0, :]

	def getFutureChoice(self):
		"""Get the future choices of the group based on each person's influence and their votes."""
		for i in range(self.numCurrentChoices):
			(self.futureChoice)[i] = np.dot((self.influence), (self.currentVote)[:, i])

	def getChoiceRanks(self):
		"""Get and return the rankings for choices made by group."""
		ranks = self.futureChoice
		ranks = self.futureChoice / sum(self.futureChoice)
		return ranks

	def findGroupChoice(self):
		self.findSimilarities()
		self.findTrust()
		self.getInfluence()
		self.getFutureChoice()
		rankings = self.getChoiceRanks()
		return rankings

if __name__ == "__main__":
	numPeoplePrompt = ("Number of people voting: ")
	pastChoicesPrompt = ("Number of choices made by this group of people in the past: ")
	currentChoicesPrompt = ("Number of choices currently being made by this group: ")
	pastVotePrompt = ("Enter the values of the past votes array as they appear row-wise: "
						)
	currentVotePrompt = ("Enter the values of the current votes array as they appear row-wise: ")
	
	numPeople = int(input(numPeoplePrompt))
	numPastChoices = int(input(pastChoicesPrompt))
	numCurrentChoices = int(input(currentChoicesPrompt))


	print(pastVotePrompt)
	# Creates then fills past votes array.
	pastVote = np.zeros((numPeople, numPastChoices))
	for i in range(numPeople):
		for j in range(numPastChoices):
			pastVote[i][j] = int(input())
	nppastVote = np.asanyarray(pastVote)

	print(currentVotePrompt)
	# Creates then fills current votes array.
	currentVote = np.zeros((numPeople, numCurrentChoices))
	for i in range(numPeople):
		for j in range(numCurrentChoices):
			currentVote[i][j] = int(input())
	npcurrentVote = np.asanyarray(currentVote)

	print("Past Votes: ", nppastVote)
	print("Current Votes: ", npcurrentVote)

	deGrootGroup = DeGroot(nppastVote, npcurrentVote)
	rankings = deGrootGroup.findGroupChoice()

	print("Group Rankings: ", rankings)