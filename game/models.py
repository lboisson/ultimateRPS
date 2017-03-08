from django.db import models
from django.contrib.auth.models import User

HANDS = (
    (u'1', u'ROCK'),
    (u'2', u'PAPER'),
    (u'3', u'SCISSORS'),
)

class Game(models.Model):
	PlayerOne = models.ForeignKey(User, related_name='PlayerOne', null=True)
	PlayerTwo = models.ForeignKey(User, related_name='PlayerTwo',null=True)
	PlayerOneHand = models.CharField(max_length=1, choices=HANDS, default='ROCK')
	PlayerTwoHand = models.CharField(max_length=1, choices=HANDS, default='ROCK')
	Date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "partie "+str(self.id)
