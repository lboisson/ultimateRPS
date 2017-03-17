from django.shortcuts import render
from game.models import Game
from django.contrib.auth.models import User
from django.db.models import Q

def compte(request):
    return render(request, 'compte/compte.html')

def notifications(request):

	if request.user.is_authenticated():
		parties = Game.objects.all() 
		return render(request, 'compte/notifications.html', {'liste_parties' : parties})
