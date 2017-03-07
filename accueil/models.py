from django.db import models

DEFAULT_PLAYER = 0

class Player(models.Model):
	PlayerName = models.CharField(max_length=100)
	Date = models.DateTimeField(auto_now_add=True, auto_now=False)
	def __str__(self):
		return self.PlayerName

class Game(models.Model):
	PlayerOne = models.ForeignKey('Player', related_name='PlayerOne', default=DEFAULT_PLAYER)
	PlayerTwo = models.ForeignKey('Player', related_name='PlayerTwo', default=DEFAULT_PLAYER)
	PlayerOneHand = models.CharField(max_length=100, default ="")
	PlayerTwoHand = models.CharField(max_length=100, default="")
	Date = models.DateTimeField(auto_now_add=True, auto_now=False)
	def __str__(self):
		return self.GameID