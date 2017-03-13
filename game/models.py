from django.db import models
from django.contrib.auth.models import User

NULL = 'Null'
ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
HANDS = (
	(NULL, 'Null'),
	(ROCK, 'Rock'),
	(PAPER, 'Paper'),
	(SCISSORS, 'Scissors'),
)

class Game(models.Model):
	PlayerOne = models.ForeignKey(User, related_name='PlayerOne', null=True)
	PlayerTwo = models.ForeignKey(User, related_name='PlayerTwo', null=True)
	PlayerOneHand = models.CharField(max_length=10, choices=HANDS, default=NULL)
	PlayerTwoHand = models.CharField(max_length=10, choices=HANDS, default=NULL)
	Date = models.DateTimeField(auto_now_add=True)
	#Outcome = models.ForeignKey(User, related_name='Winner', blank=True, null=True)
	

#	surchage de save, pas necessaire a priori
#
#	def save(self):
#		if 	not self.Outcome :
#			if self.PlayerTwoHand is ROCK :
#				if self.PlayerOneHand is ROCK :
#					self.Outcome = null
#				elif self.PlayerOneHand is PAPER :
#					self.Outcome = self.PlayerOne
#				elif self.PlayerOneHand is SCISSORS :
#					self.Outcome = self.PlayerTwo
#
#			elif self.PlayerTwoHand is PAPER :
#				if self.PlayerOneHand is ROCK :
#					self.Outcome = self.PlayerTwo
#				elif self.PlayerOneHand is PAPER :
#					self.Outcome = null
#				elif self.PlayerOneHand is SCISSORS :
#					self.Outcome = self.PlayerOne
#
#			elif self.PlayerTwoHand is SCISSORS :
#				if self.PlayerOneHand is ROCK :
#					self.Outcome = self.PlayerOne
#				elif self.PlayerOneHand is PAPER :
#					self.Outcome = self.PlayerTwo
#				elif self.PlayerOneHand is SCISSORS :
#					self.Outcome = null
#		super(Game, self).save()

	
	def _get_winner(self):
		if not self.Outcome :
			if self.PlayerTwoHand is ROCK :
				if self.PlayerOneHand is ROCK :
					return null
				elif self.PlayerOneHand is PAPER :
					return self.PlayerOne
				elif self.PlayerOneHand is SCISSORS :
					return self.PlayerTwo

			elif self.PlayerTwoHand is PAPER :
				if self.PlayerOneHand is ROCK :
					return self.PlayerTwo
				elif self.PlayerOneHand is PAPER :
					return null
				elif self.PlayerOneHand is SCISSORS :
					return self.PlayerOne

			elif self.PlayerTwoHand is SCISSORS :
				if self.PlayerOneHand is ROCK :
					return self.PlayerOne
				elif self.PlayerOneHand is PAPER :
					return self.PlayerTwo
				elif self.PlayerOneHand is SCISSORS :
					return null

	Outcome = property(_get_winner)


	def __str__(self):
		return "partie "+str(self.id)
