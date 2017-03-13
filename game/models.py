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

	Creator = models.ForeignKey(
		User, related_name='creator', null=True)
	Opponent = models.ForeignKey(
		User, related_name='opponent', null=True, blank=True)
	CreatorHand = models.CharField(
		max_length=10, choices=HANDS, default=NULL)
	OpponentHand = models.CharField(
		max_length=10, choices=HANDS, default=NULL)
	Winner = models.ForeignKey(
		User, related_name='winner', null=True, blank=True)

	# dates
	completed = models.DateTimeField(
		null=True, blank=True)
	created = models.DateTimeField(
		auto_now_add=True)
	modified = models.DateTimeField(
		auto_now=True)

	def __str__(self):
		return "partie "+str(self.id)

	#renvoie les parties en cours
	@staticmethod
	def get_available_games():
		return Game.objects.filter(opponent=None, completed=None)

	#renvoie le nombre de parties crees par l'user en parametre
	@staticmethod
	def created_count(user):
		return Game.objects.filter(creator=user).count()

	#renvoie toutes les parties qui concernent l'user
	@staticmethod
	def get_games_for_player(user):
		from django.db.models import Q
		return Game.objects.filter(Q(opponent=user) | Q(creator=user))


	#renvoie une partie selon son id
	@staticmethod
	def get_by_id(id):
		try:
			return Game.objects.get(pk=id)
		except Game.DoesNotExist:
			DEBUG_PROPAGATE_EXCEPTIONS = False
		pass

	#cree une nouvelle partie
	@staticmethod
	def create_new(user1, user2, hand):
		#user1 : le joueur qui cree la partie
		#user2 : le joueur adverse
		#hand : ce que joue le joueur
		#renvoie la partie

		new_game = Game(Creator=user1, Opponent=user2, CreatorHand=hand)
		new_game.save()

		return new_game

	# enregistre le vainqueur, et note la date de fin
	def enregistre_victoire(self, winner):
		
		self.winner = winner
		self.completed = datetime.now()
		self.save()

	# reponse de l'opponent 
	@staticmethod
	def answer(self, user, hand):
		#user : le joueur qui repond
		#hand : ce que repond le joueur2
		self.OpponentHand = hand

		if self.OpponentHand is ROCK :
			if self.CreatorHand is ROCK :
				self.outcome = null
			elif self.CreatorHand is PAPER :
				self.outcome = self.Creator
			elif self.CreatorHand is SCISSORS :
				self.outcome = self.Opponent
		elif self.OpponentHand is PAPER :
			if self.CreatorHand is ROCK :
				self.outcome = self.Opponent
			elif self.CreatorHand is PAPER :
				self.outcome = null
			elif self.CreatorHand is SCISSORS :
				self.outcome = self.Creator
		elif self.OpponentHand is SCISSORS :
			if self.CreatorHand is ROCK :
				self.outcome = self.Creator
			elif self.CreatorHand is PAPER :
				self.outcome = self.Opponent
			elif self.CreatorHand is SCISSORS :
				self.outcome = null

		self.Game.enregistre_victoire(winner=user)
