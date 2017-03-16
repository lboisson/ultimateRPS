from django.shortcuts import render
from game.models import Game
from django.db.models import Q

def compte(request):
    return render(request, 'compte/compte.html')

def notifications(request):

	if request.user.is_authenticated():
		criterion1 = Q(Creator=request.user)
		criterion2 = Q(Game__OpponentHand=True)
		parties = Game.objects.filter(criterion1 & criterion2)
		return render(request, 'compte/notifications.html', {'liste_parties' : parties})
